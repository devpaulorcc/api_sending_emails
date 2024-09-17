# Email API Project

This project provides an API for sending emails. The API allows sending emails using parameters provided in the URL, utilizing a custom script to handle email sending via SMTP.

## API Documentation

| Method | Endpoint                                          | Description                                    |
| ------ | ------------------------------------------------- | ---------------------------------------------- |
| `GET`  | `api/status`                                      | Returns the status of the API. Returns 200 for a successful connection. |
| `GET`  | `api/send/<str:sender>/<str:password_app>/<str:recipient>/<str:subject>/<str:message>` | Sends an email using the provided parameters. |

## Base URL

```bash
https://paulorcc.pythonanywhere.com/
