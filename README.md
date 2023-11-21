# CRYPTO-HUB

## Table of Contents

- [CRYPTO-HUB](#crypto-hub)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technology Stack](#technology-stack)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Configuration](#configuration)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Introduction

The Telegram bot utilizes a crypto API to provide users with real-time data on cryptocurrency,
including current prices, transaction volumes, and other relevant coin-specific information.

## Features

1. **Real-time Price Updates:** Stay informed with up-to-the-minute cryptocurrency prices.
2. **News Feed Integration:** Receive the latest news about the cryptocurrency market.
3. **User Queries:** Interact with the bot to get information about specific cryptocurrencies.

## Technology Stack

Before you begin, ensure you have the following:

1. **Python (Python3):** The primary programming language for the bot.
2. **Flask:** A micro web framework built in Python.
3. **Python-telegram-bot:** A Telegram API wrapper in Python.
4. **Requests:** A popular Python HTTP library.
5. **Telegram:** The messaging platform used to host the bot.
6. **Heroku:** A cloud platform used for deployment.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

1. [Python 3](./https://www.python.org/downloads/)
2. [Flask](./https://flask.palletsprojects.com/en/2.0.x/installation/)
3. [python-telegram-bot](./https://docs.python-telegram-bot.org/en/stable/)
4. [Requests](./https://docs.python-requests.org/en/latest/user/install/)
5. [Telegram account](./https://telegram.org/)
6. [Heroku account](./https://signup.heroku.com/)

### Installation

1. Clone this repository to your local machine.

    ```bash
    git clone <https://github.com/your-username/Crypto_Hub.git>
    cd Crypto_Hub
    ```

2. Install the required dependencies.

    ```bash
    pip install -r requirements.txt  # For Python
    ```

3. Install Heroku CLI for deployment. Follow the instructions on the [Heroku website](./https://devcenter.heroku.com/articles/heroku-cli) to install the CLI for your operating system.

    ```bash
    heroku login
    ```

### Configuration

1. Create a new Telegram bot on [BotFather](./https://core.telegram.org/bots#botfather).
2. Note down the token provided by BotFather.
3. Obtain API keys for cryptocurrency data from providers such as CoinGecko or CoinMarketCap.
4. Configure your bot by creating a `.env` file with the following content:

    ```env
    TELEGRAM_BOT_TOKEN=your-telegram-bot-token
    CRYPTO_API_KEY=your-crypto-api-key
    ```

## Usage

1. Run your bot application.

    ```bash
    Replace with your startup command
    python bot.py  # For Python
    ```

2. Start a chat with your bot on Telegram.
3. Use the available commands to interact with the bot and receive cryptocurrency information.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.

## License

This project is licensed under the [MIT License](./https://chat.openai.com/c/LICENSE).

## Acknowledgments

Special thanks to the creators of the Telegram API and cryptocurrency data providers.

1. Brian Kin Maleek (<maleekmalik@gmail.com>)
2. Esther Wachuka (<estherwachukangaru@gmail.com>)
