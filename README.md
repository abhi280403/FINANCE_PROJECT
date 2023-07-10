
# Option_Price_Simulator

The Option Price Simulator is a Django project that implements the N-step binomial tree and Black-Scholes equation methods for calculating the prices of call and put options. This simulator provides a user-friendly interface where users can input the option parameters and obtain the corresponding option prices.


## Features

- Option price calculation using the N-step binomial tree method for both call option and put option.
- Option price calculation using the Black-Scholes equation method for both call option and put option.
- Interactive web interface to input option parameters and view calculated prices.



## Installation

Clone the repository

```bash
 git clone https://github.com/abhi280403/Option_Price_Simulator.git
```
    
change into the project directory

```bash
cd Option-Price-Simulator
```
Install the required Dependencies

```bash
pip install -r requirements.txt
```


## Usage

start the development sever

```bash
python manage.py runserver
```
- Access the option price simulator in your browser at http://localhost:8000

- Choose the Call or Put option

- Choose the calculation method (N-step binomial tree or Black-Scholes equation)

- Fill in the input fields with the desired option parameters, such as underlying price, strike price, interest rate, volatility, and time to expiry.

- Click the "Submit" button to obtain the option price.

- The calculated option price will be displayed on the screen

## Screenshots
Homepage to choose Call Option or Put Option 
![Screenshot 2023-07-10 172354](https://github.com/abhi280403/Option_Price_Simulator/assets/122891629/339c37b0-c5c0-49e1-8dbc-3d8ac20bd5fa)

Call Option
![Screenshot 2023-07-10 172427](https://github.com/abhi280403/Option_Price_Simulator/assets/122891629/6f94ca81-4b6b-4533-a4ef-cdc697ccd582)
![Screenshot 2023-07-10 172444](https://github.com/abhi280403/Option_Price_Simulator/assets/122891629/e836fdfa-82ea-49ec-912c-941323c7f7f1)


Output
![Screenshot 2023-07-10 172513](https://github.com/abhi280403/Option_Price_Simulator/assets/122891629/03ee3ba4-989b-4644-8357-ce4836ec4c10)
![Screenshot 2023-07-10 172526](https://github.com/abhi280403/Option_Price_Simulator/assets/122891629/d6c22500-f233-41ba-8233-d645631fe882)



