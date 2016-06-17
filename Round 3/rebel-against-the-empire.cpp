// Copyright (c) 2016 kamyu. All rights reserved.

/*
 * Google Code Jam 2016 Round 3 - Problem C. Rebel Against The Empire
 * https://code.google.com/codejam/contest/3224486/dashboard#s=p2
 *
 * Time:  O(logN * (N^2 + H * N)), H is the length of possible planets in the timeline. (Height of BFS)
 * Space: O(N^2)
 *
 */

#include <iostream>
#include <queue>
#include <cmath>
#include <algorithm>
#include <limits>

using std::queue;
using std::cin;
using std::cout;
using std::endl;
using std::ios;
using std::min;
using std::max;
using std::log2;
using std::numeric_limits;

const int MAX_N = 1000;
const double PRECISION = 1e-4;
const int START = 0, END = 1;

int N, S;
int x[MAX_N], y[MAX_N], z[MAX_N], vx[MAX_N], vy[MAX_N], vz[MAX_N];

double jump_begin[MAX_N][MAX_N], jump_end[MAX_N][MAX_N];
double stay_begin[MAX_N], stay_end[MAX_N];

bool compare(const double D) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i != j) {
                // (vi - vj)t + pi - pj <= d
                // At^2 + Bt + (C-D) <= 0
                // (-B - sqrt(B^2 - 4(C-D))) / 2A <= t,
                // t <= (-B + sqrt(B^2 - 4(C-T))) / 2A
                double A = (vx[i] - vx[j]) * (vx[i] - vx[j]) +
                           (vy[i] - vy[j]) * (vy[i] - vy[j]) +
                           (vz[i] - vz[j]) * (vz[i] - vz[j]);
                double B = 2 * (x[i] - x[j]) * (vx[i] - vx[j]) +
                           2 * (y[i] - y[j]) * (vy[i] - vy[j]) +
                           2 * (z[i] - z[j]) * (vz[i] - vz[j]);
                double C = (x[i] - x[j]) * (x[i] - x[j]) +
                           (y[i] - y[j]) * (y[i] - y[j]) +
                           (z[i] - z[j]) * (z[i] - z[j]);
                jump_begin[i][j] = numeric_limits<double>::max();
                jump_end[i][j] = numeric_limits<double>::min();
                if (A == 0) {  // B == 0 too
                    if (C <= D) {
                        jump_begin[i][j] = 0;
                        jump_end[i][j] = numeric_limits<double>::max();
                    }
                } else {
                    if (B * B - 4 * A * (C - D) >= 0) {
                        jump_begin[i][j] =
                            (-B - sqrt(B * B - 4 * A * (C - D))) / 2 / A;
                        jump_end[i][j] =
                            (-B + sqrt(B * B - 4 * A * (C - D))) / 2 / A;
                    }
                }
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        stay_begin[i] = numeric_limits<double>::max();
        stay_end[i] = numeric_limits<double>::min();
    }
    stay_begin[0] = 0;
    stay_end[0] = S;

    // BFS
    queue<int> q;
    q.emplace(START);
    while (!q.empty()) {
        auto i = q.front();
        q.pop();
        for (int j = 0; j < N; ++j) {
            if (j != i && jump_begin[i][j] < jump_end[i][j]) {
                auto L = max(stay_begin[i], jump_begin[i][j]);
                auto R = min(stay_end[i], jump_end[i][j]);
                if (L <= R) {
                    if (j == END) {
                        return true;
                    }
                    R = jump_end[i][j];
                    if (L < stay_begin[j] || R + S > stay_end[j]) {
                        // Add unvisited / updated planet to queue.
                        stay_begin[j] = min(stay_begin[j], L);
                        stay_end[j] = max(stay_end[j], R + S);
                        q.emplace(j);
                    }
                }
            }
        }
    }

    return false;
}

double rebel_against_the_empire() {
    cin >> N >> S;
    for (int i = 0; i < N; ++i) {
        cin >>  x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
    }
    double left = 0, right = 3 * 1000 * 1000;
    const int times = log2((right - left) / (PRECISION * PRECISION)) + 1;
    for (int i = 0; i < times; ++i) {
        const auto mid = left + (right - left) / 2;
        if (compare(mid)) {
            right = mid;
        } else {
            left = mid;
        }
    }
    return sqrt(right);
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(5);
        cout << "Case #" << test << ": "
             << rebel_against_the_empire() << endl;
    }
    return 0;
}
