# 🇪🇹 Ethiopian Passport Status Checker

A Telegram bot that allows users to check the status of their Ethiopian passport application by providing their application number.

The bot retrieves the application information from the Ethiopian Passport Services system and displays the available passport, payment, appointment, and delivery details directly in Telegram.

---

## Features

- 🔎 Check passport application status
- 🆔 Search using an application number
- 👤 Display applicant information
- 💳 Display payment status
- 📄 Display passport page information
- 📅 Display appointment date
- 📍 Display appointment office
- 🚚 Display delivery date
- 📦 Display delivery site
- 🤖 Telegram bot interface

---

## Tech Stack

- Python
- pyTelegramBotAPI
- Requests
- Ethiopian Passport Services API

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sigmaCoderx/passportStatusChecker.git
cd passportStatusChecker
```

### Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Telegram Bot Token

Create a Telegram bot using **BotFather**:

https://t.me/BotFather

Add your bot token to:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
```

---

## Running the Bot

```bash
python main.py
```

The bot will start polling for incoming messages.

---

## How It Works

1. Start the bot using `/start`.
2. Send your passport application number.
3. The bot sends the application number to the Ethiopian Passport Services API.
4. The API response is processed.
5. The bot displays the available application information.

---

## Example

### Start

```text
/start
```

The bot responds with instructions to provide an application number beginning with `M`.

### Input

```text
MXXXXXXXX
```

### Response

```text
Application number: MXXXXXXXX

Full Name: Applicant Name

Payment Status: ...

Passport page: ...

Appointment date: ...

Appointment place: ...

Delivery date: ...

Delivery site/place: ...
```

---

## Information Retrieved

The bot attempts to retrieve and display:

| Information | Description |
|---|---|
| Application Number | Passport application identifier |
| Full Name | Applicant's first, middle, and last name |
| Payment Status | Current payment/request status |
| Passport Page | Passport page information |
| Appointment Date | Scheduled appointment date |
| Appointment Place | Appointment office |
| Delivery Date | Expected delivery date |
| Delivery Site | Passport delivery location |

---

## Project Structure

```text
passportStatusChecker/
├── main.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## Requirements

All Python dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## Deployment

The project includes a `Procfile` for platforms that support Procfile-based deployments.

Example:

```text
worker: python main.py
```

---

## Notes

- Requires a valid Telegram Bot Token.
- Requires an active internet connection.
- Requires a valid passport application number.
- The bot depends on the availability and behavior of the Ethiopian Passport Services API.
- API authentication details may expire or change over time.
- Never commit your Telegram Bot Token or API credentials to GitHub.

---

## License

MIT License

---

## Author

**flippedCoin**

GitHub: https://github.com/sigmaCoderx
