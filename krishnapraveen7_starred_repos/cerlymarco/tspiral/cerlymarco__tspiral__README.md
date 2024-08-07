# [tspiral](https://github.com/cerlymarco/tspiral)

# tspiral
A python package for time series forecasting with scikit-learn estimators.

tspiral is not a library that works as a wrapper for other tools and methods for time series forecasting. tspiral directly provides scikit-learn estimators for time series forecasting. It leverages the benefit of using scikit-learn syntax and components to easily access the open source ecosystem built on top of the scikit-learn community. It easily maps a complex time series forecasting problems into a tabular supervised regression task, solving it with a standard approach. 

## Overview

tspiral provides 4 optimized forecasting techniques:

- **Recursive Forecasting** 

Lagged target features are combined with exogenous regressors (if provided) and lagged exogenous features (if specified). A scikit-learn compatible regressor is fitted on the whole merged data. The fitted estimator is called iteratively to predict multiple steps ahead.

![recursive-standard](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/recursive-standard.PNG)

Which in a compact way we can summarize in:

![recursive-compact](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/recursive-compact.PNG)

- **Direct Forecasting** 

A scikit-learn compatible regressor is fitted on the lagged data for each time step to forecast. 

![direct](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/direct.PNG)

Which in a compact way we can summarize in:

![direct-compact](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/direct-compact.png)

It's also possible to mix recursive and direct forecasting by predicting directly some future horizons while using recursive on the remaining. 

![directmix-compact](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/directmix-compact.png)

- **Stacking Forecasting** 

Multiple recursive time series forecasters are fitted and combined on the final portion of the training data with a meta-learner.

![stacked](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/stacked.PNG)

- **Rectified Forecasting** 

Multiple direct time series forecasters are fitted and combined on the final portion of the training data with a meta-learner.

![rectify](https://raw.githubusercontent.com/cerlymarco/tspiral/master/imgs/rectify.PNG)

**GLOBAL and MULTIVARIATE time series forecasting are natively supported for all the forecasting methods available.** For GLOBAL forecasting, use the `groups` parameter to specify the column of the input data that contains the group identifiers. For MULTIVARIATE forecasting, pass a target with multiple columns when calling fit. 

## Installation
```shell
pip install --upgrade tspiral
```
The module depends only on NumPy, Pandas, and Scikit-Learn (>=0.24.2). Python 3.6 or above is supported.

## Media

- [How to Improve Recursive Time Series Forecasting](https://medium.com/towards-data-science/how-to-improve-recursive-time-series-forecasting-ff5b90a98eeb)
- [Time Series Forecasting with Feature Selection: Why you may need it](https://medium.com/towards-data-science/time-series-forecasting-with-feature-selection-why-you-may-need-it-696b23ecc329)
- [Forecast Time Series with Missing Values: Beyond Linear Interpolation](https://medium.com/towards-data-science/forecast-time-series-with-missing-values-beyond-linear-interpolation-2f2adf0a0cba)
- [Time Series Forecasting with Conformal Prediction Intervals: Scikit-Learn is All you Need](https://medium.com/towards-data-science/time-series-forecasting-with-conformal-prediction-intervals-scikit-learn-is-all-you-need-4b68143a027a)
- [Hitting Time Forecasting: The Other Way for Time Series Probabilistic Forecasting](https://medium.com/towards-data-science/hitting-time-forecasting-the-other-way-for-time-series-probabilistic-forecasting-6c3b6496c353)
- [Hitchhiker’s Guide to MLOps for Time Series Forecasting with Sklearn](https://medium.com/towards-data-science/hitchhikers-guide-to-mlops-for-time-series-forecasting-with-sklearn-d5d9728095a7)

## Usage

- **Recursive Forecasting** 
```python
import numpy as np
from sklearn.linear_model import Ridge
from tspiral.forecasting import ForecastingCascade
timesteps = 400
e = np.random.normal(0,1, (timesteps,))
y = np.concatenate([
    2*np.sin(np.arange(timesteps)*(2*np.pi/24))+e,
    2*np.cos(np.arange(timesteps)*(2*np.pi/24))+e,
])
X = [[0]]*timesteps+[[1]]*timesteps 
model = ForecastingCascade(
    Ridge(),
    lags=range(1,24+1),
    groups=[0],
).fit(X, y)
forecasts = model.predict([[0]]*80+[[1]]*80)
```

- **Direct Forecasting** 
```python
import numpy as np
from sklearn.linear_model import Ridge
from tspiral.forecasting import ForecastingChain
timesteps = 400
e = np.random.normal(0,1, (timesteps,))
y = np.concatenate([
    2*np.sin(np.arange(timesteps)*(2*np.pi/24))+e,
    2*np.cos(np.arange(timesteps)*(2*np.pi/24))+e,
])
X = [[0]]*timesteps+[[1]]*timesteps 
model = ForecastingChain(
    Ridge(),
    n_estimators=24,
    lags=range(1,24+1),
    groups=[0],
).fit(X, y)
forecasts = model.predict([[0]]*80+[[1]]*80)
```

- **Stacking Forecasting** 
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from tspiral.forecasting import ForecastingStacked
timesteps = 400
e = np.random.normal(0,1, (timesteps,))
y = np.concatenate([
    2*np.sin(np.arange(timesteps)*(2*np.pi/24))+e,
    2*np.cos(np.arange(timesteps)*(2*np.pi/24))+e,
])
X = [[0]]*timesteps+[[1]]*timesteps 
model = ForecastingStacked(
    [Ridge(), DecisionTreeRegressor()],
    test_size=24*3,
    lags=range(1,24+1),
    groups=[0],
).fit(X, y)
forecasts = model.predict([[0]]*80+[[1]]*80)
```

- **Rectified Forecasting** 
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from tspiral.forecasting import ForecastingRectified
timesteps = 400
e = np.random.normal(0,1, (timesteps,))
y = np.concatenate([
    2*np.sin(np.arange(timesteps)*(2*np.pi/24))+e,
    2*np.cos(np.arange(timesteps)*(2*np.pi/24))+e,
])
X = [[0]]*timesteps+[[1]]*timesteps  
model = ForecastingRectified(
    [Ridge(), DecisionTreeRegressor()],
    n_estimators=24*3,
    test_size=24*3,
    lags=range(1,24+1),
    groups=[0],
).fit(X, y)
forecasts = model.predict([[0]]*80+[[1]]*80)
```

More examples in the [notebooks folder](https://github.com/cerlymarco/tspiral/tree/main/notebooks).
