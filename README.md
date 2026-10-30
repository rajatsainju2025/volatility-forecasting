# Can Machine Learning Beat HAR at Forecasting Volatility?

An out-of-sample comparison of classic volatility models (HAR, GJR-GARCH, EWMA) against gradient-boosted trees (LightGBM) for forecasting next-day realized variance of the S&P 500 ETF (SPY).


# Why this problem
- A hands-on project to learn about volatuility forecasting.
- Returns are close to unpredictable, but volatility clusters: big moves follow big moves. So there is real signal, and a strong, simple baseline to beat.


# References
- Corsi, F. (2009). A simple approximate long-memory model of realized volatility. Journal of Financial Econometrics, 7(2), 174–196.
- Glosten, L., Jagannathan, R., & Runkle, D. (1993). On the relation between the expected value and the volatility of the nominal excess return on stocks. Journal of Finance, 48(5), 1779–1801.
Garman, M., & Klass, M. (1980). On the estimation of security price volatilities from historical data. Journal of Business, 53(1), 67–78.
- Patton, A. (2011). Volatility forecast comparison using imperfect volatility proxies. Journal of Econometrics, 160(1), 246–256.
- Diebold, F., & Mariano, R. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263.