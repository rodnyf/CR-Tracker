# Contribution-Room-Tracker

A tool to track your TFSA Contribution Room from Questrade,

## Installation
* Use `pip`/`pip3`:

   `pip install CR-tracker`

## Getting Started

### Get the refresh token from Questrade

1. Familiarise yourself with the [Security documentation](https://www.questrade.com/api/documentation/security) for the Questrade API.
2. [Generate](https://apphub.questrade.com/UI/UserApps.aspx) a manual refresh token 
   1. Login to [questrade.com](https://www.questrade.com/)
   2. Account Drop Down > Click 'App hub' > Click 'Register a Personal App' 
   3. Ensure 'OAuth scopes' retrieve balances, positions, orders and executions is checked 
   4. Under Personal apps, Click '+ New Device' > Click 'Generate New token' 
   5. Copy this token!
![Capture1 Apphub.PNG](CR-Tracker%2FCapture1%20Apphub.PNG)
   
### Connect to Questrade
```
   import CR_Tracker as CR
   
   CR.connect_questrade(token=ikWQKJHLKJdfdjza5a_0EyivzTJk8hfg9b0)
   ```
   **Important:**
   A token will be created at `~/.questrade.json` and used for future API calls
   * If the token is valid future initiations will not require a refresh token


If there is already a valid token, you can simply connect to questrade without declaring a token
   ```
   import CR_Tracker as CR
   CR.connect_questrade()
   ```

## Calulating your Contribution Room
#### [Contribution Room]()
Accepts: ```given_year=None, given_contr_room=None, open_year=2009, birth_year=1990, token=None```

The method that contribution_room is calculated is determined by which parameters are inputted by the user\
**FOR BEST RESULTS: Use the Contribution Room from your CRA my Account on January 1 of the given year**

Below is the hierarchy of the contribution room

1. If ```given_year``` and ```given_contr_room``` are both provided,
only account activity in the given_year and onwards will be used  
2. If either ```given_year``` or ```given_contr_room``` are not provided then the search period will be from ```open_year```
3. If ```open_year``` is not provided then the search period will start when the user turned 18 (after 2009) \
based on the ```birth_year``` 

This function will choose the **first** method above, that is available 

```open_year``` is the year that the Account was opened. Default value is 2009- when the TFSA was first introduced
```birth_year```  is the year that the user was born. Default value is 1990- those born before 1990 were 18 years old in 2009

```
x=CR.contribution_room(given_contr_room=35500,given_year=2022,token=ikWQKJHLKJdfdjza5a_0EyivzTJk8hfg9b0)
x

=> start_year is 2022
Questrade time is: {'time': '2024-01-03T17:46:46.904000-05:00'}
Successfully Connected to Questrade
TFSA  account list: ['5173xxxx', '5196xxxx', '5205xxxx']
DatetimeIndex(['2022-01-31', '2022-02-28', '2022-03-31', '2022-04-30',
               '2022-05-31', '2022-06-30', '2022-07-31', '2022-08-31',
               '2022-09-30', '2022-10-31', '2022-11-30', '2022-12-31',
               '2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30',
               '2023-05-31', '2023-06-30', '2023-07-31', '2023-08-31',
               '2023-09-30', '2023-10-31', '2023-11-30', '2023-12-31',
               '2024-01-31'],
              dtype='datetime64[ns]', freq='M')
grabbing activity from 2022-01-31 00:00:00 to 2024-01-31 00:00:00 for TFSA: 5173xxxx. Completed 0 % 
Processing 2022 for account 5173xxxx
Processing 2023 for account 5173xxxx
Processing 2024 for account 5173xxxx
grabbing activity from 2022-01-31 00:00:00 to 2024-01-31 00:00:00 for TFSA: 5196xxxx. Completed 33 % 
Processing 2022 for account 5196xxxx
Processing 2023 for account 5196xxxx
Processing 2024 for account 5196xxxx
grabbing activity from 2022-01-31 00:00:00 to 2024-01-31 00:00:00 for TFSA: 5205xxxx. Completed 66 % 
Processing 2022 for account 5205xxxx
Processing 2023 for account 5205xxxx
Processing 2024 for account 5205xxxx
Grabbing Activity Completed-100%
Today's date: 2024-01-03
Your current contribution room is: $ 9xxxxxxx.5xxxxxxx
Next Year's Contribution room on Jan 1 2025 is:  $9xxxxxxxx.5xxxxxxxxx
```
#### contribution_room returns a list of 3 items

[current contribution room, Next Year's Contribution, panda's dataframe with the summarized results ]
```
x[0]
=> 9xxxxxxx.5xxxxxxx
x[1]
=> 9xxxxxxx.5xxxxxxx
x[2]
=> 
| New_Year_Dollar_Limit | Contr_Room_Jan1 | Year | Deposits | Withdrawals | Current_Contr_Room |
```