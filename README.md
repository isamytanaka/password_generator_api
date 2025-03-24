## Password Generator API
![](https://raw.githubusercontent.com/isamytanaka/password_generator_api/31d6611f2a3d246ee6982f0f3bc7e7baf8576c6f/password-svgrepo-com%20(1).svg)
> This **API** generates random passwords with customizable options. Users can specify the length of the password and whether to include numbers and special characters.

**Base URL:**

http://122.0.1.1:5000

**Endpoint:**

`GET /generate_password`

## Query Parameters:

| Parameter   | Type    | Default | Description                          |
|-------------|---------|---------|--------------------------------------|
| `length`    | `int`   | `12`    | Length of the generated password.    |
| `numbers`   | `bool`  | `true`  | Include numbers (0-9).               |
| `specials`  | `bool`  | `true`  | Include special characters (`!@#...`). |

## Example Request:

``http://122.0.1.1:5000/generate_password?length=16&numbers=true&specials=false``

Example Response (JSON):

`{
    "password": "AbCdEfGh123456"
}`

> This API is useful for generating strong passwords for secure authentication.
