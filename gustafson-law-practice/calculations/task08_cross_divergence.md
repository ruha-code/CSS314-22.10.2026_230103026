# Amdahl and Gustafson at 128 processors

Given `s = α = 0.08` and `P = 128`:

\[
S_A=\frac{1}{s+(1-s)/P}
   =\frac{1}{0.08+0.92/128}
   \approx 11.47.
\]

\[
S_G=P-\alpha(P-1)
   =128-0.08(127)
   =117.84.
\]

Using Amdahl's result as the baseline, the percentage difference is

\[
\frac{S_G-S_A}{S_A}\times100\%
\approx 927.4\%.
\]

Gustafson's result is about `10.27` times Amdahl's result. They differ because Amdahl keeps the total job fixed, while Gustafson increases the parallel work as processors are added.
