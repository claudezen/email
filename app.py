from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from flask_mail import Mail, Message
import re
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import jwt
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["SECRET_KEY"] = (
    "gtx9910645c36eebf1e69dd827e825e63de474c00ff27e40ec2045ec8614432b"
)

# Email configuration
app.config['MAIL_SERVER'] = 'libra.vivawebhost.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'no-reply@gtx.com.co'
app.config['MAIL_PASSWORD'] = '9lmZ=[4M%$Ut'
app.config['MAIL_DEFAULT_SENDER'] = 'no-reply@gtx.com.co'

mail = Mail(app)


def init_db():
    conn = sqlite3.connect("gtx.db")
    c = conn.cursor()

    # Users table
    c.execute(
        """CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  first_name TEXT,
                  last_name TEXT,
                  mobile_number TEXT,
                  created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  profile_picture TEXT,
                  is_verified BOOLEAN DEFAULT FALSE)"""
    )

    # Newsletter table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS newsletter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL
        )
    """
    )

    # Notification table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS notification (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL
        )
    """
    )

    # Verification table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS verification (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()
    conn.close()


init_db()


# Helper functions
def get_db_connection():
    conn = sqlite3.connect("gtx.db")
    conn.row_factory = sqlite3.Row
    return conn


def generate_token(user_id):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        "iat": datetime.datetime.utcnow(),
        "sub": user_id,
    }
    return jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")


def is_valid_email(email):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    return re.match(email_regex, email) is not None


def send_email(to_email, subject, html_content):
    try:
        msg = Message(subject, recipients=[to_email], html=html_content)
        mail.send(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")



# Routes
@app.route("/", methods=["GET"])
def index():
    return "Welcome to the GTX API."


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"message": "Username, email, and password are required"}), 400

    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    if len(password) < 8:
        return jsonify({"message": "Password must be at least 8 characters long"}), 400

    hashed_password = generate_password_hash(password)

    try:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        user_id = conn.execute(
            "SELECT id FROM users WHERE email = ?", (email,)
        ).fetchone()["id"]

        # Generate verification token
        token = generate_token(user_id)
        verification_link = f"https://gtx.pythonanywhere.com/verify/{token}"

        # Create the email template
        email_template = f"""
        <!DOCTYPE html
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!--<![endif]-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="format-detection" content="date=no" />
  <meta name="format-detection" content="address=no" />
  <meta name="format-detection" content="email=no" />
  <meta name="x-apple-disable-message-reformatting" />
  <link href="https://fonts.googleapis.com/css?family=Poppins:ital,wght@0,400;0,500" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css?family=Cinzel:ital,wght@0,400" rel="stylesheet" />
  <title>Welcome to GTX!</title>
  <style>
    html,
    body {{
      margin: 0 !important;
      padding: 0 !important;
      min-height: 100% !important;
      width: 100% !important;
      -webkit-font-smoothing: antialiased;
    }}

    * {{
      -ms-text-size-adjust: 100%;
    }}

    #outlook a {{
      padding: 0;
    }}

    .ReadMsgBody,
    .ExternalClass {{
      width: 100%;
    }}

    .ExternalClass,
    .ExternalClass p,
    .ExternalClass td,
    .ExternalClass div,
    .ExternalClass span,
    .ExternalClass font {{
      line-height: 100%;
    }}

    table,
    td,
    th {{
      mso-table-lspace: 0 !important;
      mso-table-rspace: 0 !important;
      border-collapse: collapse;
    }}

    u+.body table,
    u+.body td,
    u+.body th {{
      will-change: transform;
    }}

    body,
    td,
    th,
    p,
    div,
    li,
    a,
    span {{
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
      mso-line-height-rule: exactly;
    }}

    img {{
      border: 0;
      outline: 0;
      line-height: 100%;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }}

    a[x-apple-data-detectors] {{
      color: inherit !important;
      text-decoration: none !important;
    }}

    .pc-gmail-fix {{
      display: none;
      display: none !important;
    }}

    .body .pc-project-body {{
      background-color: transparent !important;
    }}

    @media (min-width: 621px) {{
      .pc-lg-hide {{
        display: none;
      }}

      .pc-lg-bg-img-hide {{
        background-image: none !important;
      }}
    }}
  </style>
  <style>
    @media (max-width: 620px) {{
      .pc-project-body {{
        min-width: 0px !important;
      }}

      .pc-project-container {{
        width: 100% !important;
      }}

      .pc-sm-hide {{
        display: none !important;
      }}

      .pc-sm-bg-img-hide {{
        background-image: none !important;
      }}

      .pc-w620-padding-0-0-0-0 {{
        padding: 0px 0px 0px 0px !important;
      }}

      table.pc-w620-spacing-24-0-24-0 {{
        margin: 24px 0px 24px 0px !important;
      }}

      td.pc-w620-spacing-24-0-24-0,
      th.pc-w620-spacing-24-0-24-0 {{
        margin: 0 !important;
        padding: 24px 0px 24px 0px !important;
      }}

      .pc-w620-width-100 {{
        width: 100px !important;
      }}

      .pc-w620-height-auto {{
        height: auto !important;
      }}

      .pc-w620-itemsSpacings-18-0 {{
        padding-left: 9px !important;
        padding-right: 9px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
      }}

      .pc-w620-width-hug {{
        width: auto !important;
      }}

      table.pc-w620-spacing-0-0-24-0 {{
        margin: 0px 0px 24px 0px !important;
      }}

      td.pc-w620-spacing-0-0-24-0,
      th.pc-w620-spacing-0-0-24-0 {{
        margin: 0 !important;
        padding: 0px 0px 24px 0px !important;
      }}

      .pc-w620-width-101 {{
        width: 101px !important;
      }}

      table.pc-w620-spacing-0-0-0-0 {{
        margin: 0px 0px 0px 0px !important;
      }}

      td.pc-w620-spacing-0-0-0-0,
      th.pc-w620-spacing-0-0-0-0 {{
        margin: 0 !important;
        padding: 0px 0px 0px 0px !important;
      }}

      div.pc-w620-textAlign-center,
      th.pc-w620-textAlign-center,
      a.pc-w620-textAlign-center,
      td.pc-w620-textAlign-center {{
        text-align: center !important;
        text-align-last: center !important;
      }}

      table.pc-w620-textAlign-center {{
        float: none !important;
        margin-right: auto !important;
        margin-left: auto !important;
      }}

      img.pc-w620-textAlign-center {{
        margin-right: auto !important;
        margin-left: auto !important;
      }}

      .pc-w620-width-73 {{
        width: 73px !important;
      }}

      .pc-w620-padding-8-24-24-24 {{
        padding: 8px 24px 24px 24px !important;
      }}

      .pc-w620-width-78pc {{
        width: 78% !important;
      }}

      .pc-w620-fontSize-40px {{
        font-size: 40px !important;
      }}

      .pc-w620-lineHeight-40 {{
        line-height: 40px !important;
      }}

      table.pc-w620-spacing-0-0-32-0 {{
        margin: 0px 0px 32px 0px !important;
      }}

      td.pc-w620-spacing-0-0-32-0,
      th.pc-w620-spacing-0-0-32-0 {{
        margin: 0 !important;
        padding: 0px 0px 32px 0px !important;
      }}

      .pc-w620-fontSize-15px {{
        font-size: 15px !important;
      }}

      .pc-w620-lineHeight-139pc {{
        line-height: 139% !important;
      }}

      .pc-w620-padding-24-24-48-24 {{
        padding: 24px 24px 48px 24px !important;
      }}

      .pc-w620-itemsSpacings-20-0 {{
        padding-left: 10px !important;
        padding-right: 10px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
      }}

      .pc-w620-fontSize-13px {{
        font-size: 13px !important;
      }}

      .pc-w620-width-270 {{
        width: 270px !important;
      }}

      .pc-w620-height-1 {{
        height: 1px !important;
      }}

      .pc-w620-padding-30-24-30-24 {{
        padding: 30px 24px 30px 24px !important;
      }}

      .pc-w620-gridCollapsed-1>tbody,
      .pc-w620-gridCollapsed-1>tbody>tr,
      .pc-w620-gridCollapsed-1>tr {{
        display: inline-block !important;
      }}

      .pc-w620-gridCollapsed-1.pc-width-fill>tbody,
      .pc-w620-gridCollapsed-1.pc-width-fill>tbody>tr,
      .pc-w620-gridCollapsed-1.pc-width-fill>tr {{
        width: 100% !important;
      }}

      .pc-w620-gridCollapsed-1.pc-w620-width-fill>tbody,
      .pc-w620-gridCollapsed-1.pc-w620-width-fill>tbody>tr,
      .pc-w620-gridCollapsed-1.pc-w620-width-fill>tr {{
        width: 100% !important;
      }}

      .pc-w620-gridCollapsed-1>tbody>tr>td,
      .pc-w620-gridCollapsed-1>tr>td {{
        display: block !important;
        width: auto !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
      }}

      .pc-w620-gridCollapsed-1.pc-width-fill>tbody>tr>td,
      .pc-w620-gridCollapsed-1.pc-width-fill>tr>td {{
        width: 100% !important;
      }}

      .pc-w620-gridCollapsed-1.pc-w620-width-fill>tbody>tr>td,
      .pc-w620-gridCollapsed-1.pc-w620-width-fill>tr>td {{
        width: 100% !important;
      }}

      .pc-w620-gridCollapsed-1>tbody>.pc-grid-tr-first>.pc-grid-td-first,
      pc-w620-gridCollapsed-1>.pc-grid-tr-first>.pc-grid-td-first {{
        padding-top: 0 !important;
      }}

      .pc-w620-gridCollapsed-1>tbody>.pc-grid-tr-last>.pc-grid-td-last,
      pc-w620-gridCollapsed-1>.pc-grid-tr-last>.pc-grid-td-last {{
        padding-bottom: 0 !important;
      }}

      .pc-w620-gridCollapsed-0>tbody>.pc-grid-tr-first>td,
      .pc-w620-gridCollapsed-0>.pc-grid-tr-first>td {{
        padding-top: 0 !important;
      }}

      .pc-w620-gridCollapsed-0>tbody>.pc-grid-tr-last>td,
      .pc-w620-gridCollapsed-0>.pc-grid-tr-last>td {{
        padding-bottom: 0 !important;
      }}

      .pc-w620-gridCollapsed-0>tbody>tr>.pc-grid-td-first,
      .pc-w620-gridCollapsed-0>tr>.pc-grid-td-first {{
        padding-left: 0 !important;
      }}

      .pc-w620-gridCollapsed-0>tbody>tr>.pc-grid-td-last,
      .pc-w620-gridCollapsed-0>tr>.pc-grid-td-last {{
        padding-right: 0 !important;
      }}

      .pc-w620-tableCollapsed-1>tbody,
      .pc-w620-tableCollapsed-1>tbody>tr,
      .pc-w620-tableCollapsed-1>tr {{
        display: block !important;
      }}

      .pc-w620-tableCollapsed-1.pc-width-fill>tbody,
      .pc-w620-tableCollapsed-1.pc-width-fill>tbody>tr,
      .pc-w620-tableCollapsed-1.pc-width-fill>tr {{
        width: 100% !important;
      }}

      .pc-w620-tableCollapsed-1.pc-w620-width-fill>tbody,
      .pc-w620-tableCollapsed-1.pc-w620-width-fill>tbody>tr,
      .pc-w620-tableCollapsed-1.pc-w620-width-fill>tr {{
        width: 100% !important;
      }}

      .pc-w620-tableCollapsed-1>tbody>tr>td,
      .pc-w620-tableCollapsed-1>tr>td {{
        display: block !important;
        width: auto !important;
      }}

      .pc-w620-tableCollapsed-1.pc-width-fill>tbody>tr>td,
      .pc-w620-tableCollapsed-1.pc-width-fill>tr>td {{
        width: 100% !important;
        box-sizing: border-box !important;
      }}

      .pc-w620-tableCollapsed-1.pc-w620-width-fill>tbody>tr>td,
      .pc-w620-tableCollapsed-1.pc-w620-width-fill>tr>td {{
        width: 100% !important;
        box-sizing: border-box !important;
      }}
    }}
  </style>
  <!--[if !mso]><!-- -->
  <style>
    @media all {{
      @font-face {{
        font-family: "Poppins";
        font-style: normal;
        font-weight: 500;
        src: url("https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1JlEw.woff") format("woff"),
          url("https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1JlFQ.woff2") format("woff2");
      }}

      @font-face {{
        font-family: "Cinzel";
        font-style: normal;
        font-weight: 400;
        src: url("https://fonts.gstatic.com/s/cinzel/v23/8vIU7ww63mVu7gtR-kwKxNvkNOjw-tbnfYPlCw.woff") format("woff"),
          url("https://fonts.gstatic.com/s/cinzel/v23/8vIU7ww63mVu7gtR-kwKxNvkNOjw-tbnfYPlDQ.woff2") format("woff2");
      }}
    }}
  </style>
  <!--<![endif]-->
  <!--[if mso]>
      <style type="text/css">
        .pc-font-alt {{
          font-family: Arial, Helvetica, sans-serif !important;
        }}
      </style>
    <![endif]-->
  <!--[if gte mso 9]>
      <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG />
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
      </xml>
    <![endif]-->
</head>

<body class="body pc-font-alt" style="
      width: 100% !important;
      min-height: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
      line-height: 1.5;
      color: #2d3a41;
      mso-line-height-rule: exactly;
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
      font-variant-ligatures: normal;
      text-rendering: optimizeLegibility;
      -moz-osx-font-smoothing: grayscale;
      background-color: #fbf4ee;
    " bgcolor="#fbf4ee">
  <table class="pc-project-body" style="table-layout: fixed; min-width: 600px; background-color: #fbf4ee"
    bgcolor="#fbf4ee" width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
    <tr>
      <td align="center" valign="top">
        <table class="pc-project-container" style="width: 600px; max-width: 600px" width="600" align="center" border="0"
          cellpadding="0" cellspacing="0" role="presentation">
          <tr>
            <td class="pc-w620-padding-0-0-0-0" style="padding: 20px 0px 20px 0px" align="left" valign="top">
              <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="width: 100%">
                <tr>
                  <td valign="top">
                    <!-- BEGIN MODULE: Menu -->
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                      <tr>
                        <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px">
                          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation" style="
                                border-collapse: separate;
                                border-spacing: 0px;
                              ">
                            <tr>
                              <td valign="top" class="pc-w620-padding-8-24-24-24" style="
                                    padding: 48px 24px 0px 24px;
                                    background-color: #ffffff;
                                    box-shadow: 10px 10px 0px 0px
                                      rgba(236, 234, 232, 1);
                                  " bgcolor="#ffffff">
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td class="pc-w620-spacing-24-0-24-0" align="center" valign="top"
                                      style="padding: 0px 0px 24px 0px">
                                      <img src="https://cloudfilesdm.com/postcards/image-1720271509899.png"
                                        class="pc-w620-width-100 pc-w620-height-auto" width="120" height="39" alt="GTX"
                                        style="
                                            display: block;
                                            border: 0;
                                            outline: 0;
                                            line-height: 100%;
                                            -ms-interpolation-mode: bicubic;
                                            width: 120px;
                                            height: auto;
                                            max-width: 100%;
                                          " />
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td class="pc-w620-spacing-0-0-24-0" align="center"
                                      style="padding: 0px 0px 0px 0px">
                                      <table class="pc-width-hug pc-w620-gridCollapsed-0 pc-w620-width-hug"
                                        align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                        <tr class="pc-grid-tr-first pc-grid-tr-last">
                                          <td class="pc-grid-td-first pc-w620-itemsSpacings-18-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              ">
                                            <table class="pc-w620-width-hug" border="0" cellpadding="0" cellspacing="0"
                                              role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="left" valign="middle" style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table class="pc-w620-width-hug" align="left" border="0"
                                                    cellpadding="0" cellspacing="0" role="presentation">
                                                    <tr>
                                                      <td align="left" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation" align="left" style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            ">
                                                          <tr>
                                                            <td valign="top" align="left">
                                                              <a class="pc-font-alt" href="https://www.gtx.com.co/"
                                                                target="_blank" style="
                                                                    text-decoration: none;
                                                                    line-height: 140%;
                                                                    letter-spacing: 0.06em;
                                                                    font-family: 'Poppins',
                                                                      Arial,
                                                                      Helvetica,
                                                                      sans-serif;
                                                                    font-size: 13px;
                                                                    font-weight: 500;
                                                                    font-variant-ligatures: normal;
                                                                    color: #181818;
                                                                    text-transform: uppercase;
                                                                    text-align: left;
                                                                    text-align-last: left;
                                                                  ">
                                                                <span style="
                                                                      text-transform: uppercase;
                                                                    ">H</span><span>Ø</span><span style="
                                                                      text-transform: uppercase;
                                                                    ">ME</span>
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-18-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td class="pc-w620-spacing-0-0-0-0" valign="top">
                                                              <table border="0" cellpadding="0" cellspacing="0"
                                                                role="presentation" width="100%" style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  ">
                                                                <tr>
                                                                  <td valign="top"
                                                                    class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                    align="center" style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      ">
                                                                    <a class="pc-font-alt pc-w620-textAlign-center"
                                                                      href="https://www.gtx.com.co/#about"
                                                                      target="_blank" style="
                                                                          text-decoration: none;
                                                                          line-height: 140%;
                                                                          letter-spacing: 0.06em;
                                                                          font-family: 'Poppins',
                                                                            Arial,
                                                                            Helvetica,
                                                                            sans-serif;
                                                                          font-size: 13px;
                                                                          font-weight: 500;
                                                                          font-variant-ligatures: normal;
                                                                          color: #181818;
                                                                          text-transform: uppercase;
                                                                          text-align: center;
                                                                          text-align-last: center;
                                                                        ">
                                                                      <span style="
                                                                            text-transform: uppercase;
                                                                          ">AB</span><span>Ø</span><span style="
                                                                            text-transform: uppercase;
                                                                          ">UT
                                                                        US</span>
                                                                    </a>
                                                                  </td>
                                                                </tr>
                                                              </table>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-18-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table class="pc-w620-width-hug" border="0" cellpadding="0" cellspacing="0"
                                              role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table class="pc-w620-width-hug" align="center" border="0"
                                                    cellpadding="0" cellspacing="0" role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation" align="center" style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            ">
                                                          <tr>
                                                            <td valign="top" align="center">
                                                              <a class="pc-font-alt" href="https://www.gtx.com.co/"
                                                                target="_blank" style="
                                                                    text-decoration: none;
                                                                    line-height: 140%;
                                                                    letter-spacing: 0.06em;
                                                                    font-family: 'Poppins',
                                                                      Arial,
                                                                      Helvetica,
                                                                      sans-serif;
                                                                    font-size: 13px;
                                                                    font-weight: 500;
                                                                    font-variant-ligatures: normal;
                                                                    color: #181818;
                                                                    text-transform: uppercase;
                                                                    text-align: center;
                                                                    text-align-last: center;
                                                                  ">
                                                                <span style="
                                                                      text-transform: uppercase;
                                                                    ">Events</span>
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-18-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table class="pc-w620-width-hug" border="0" cellpadding="0" cellspacing="0"
                                              role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table class="pc-w620-width-hug" align="center" border="0"
                                                    cellpadding="0" cellspacing="0" role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation" align="center" style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            ">
                                                          <tr>
                                                            <td valign="top" align="center">
                                                              <a class="pc-font-alt" href="mailto:info@gtx.com.co"
                                                                target="_blank" style="
                                                                    text-decoration: none;
                                                                    line-height: 140%;
                                                                    letter-spacing: 0.06em;
                                                                    font-family: 'Poppins',
                                                                      Arial,
                                                                      Helvetica,
                                                                      sans-serif;
                                                                    font-size: 13px;
                                                                    font-weight: 500;
                                                                    font-variant-ligatures: normal;
                                                                    color: #181818;
                                                                    text-transform: uppercase;
                                                                    text-align: center;
                                                                    text-align-last: center;
                                                                  ">
                                                                <span style="
                                                                      text-transform: uppercase;
                                                                    ">SUPP</span><span>Ø</span><span style="
                                                                      text-transform: uppercase;
                                                                    ">RT</span>
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-grid-td-last pc-w620-itemsSpacings-18-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table class="pc-w620-width-hug" border="0" cellpadding="0" cellspacing="0"
                                              role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table class="pc-w620-width-hug" align="center" border="0"
                                                    cellpadding="0" cellspacing="0" role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation" align="center" style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            ">
                                                          <tr>
                                                            <td valign="top" align="center">
                                                              <a class="pc-font-alt" href="https://www.gtx.com.co/"
                                                                target="_blank" style="
                                                                    text-decoration: none;
                                                                    line-height: 140%;
                                                                    letter-spacing: 0.06em;
                                                                    font-family: 'Poppins',
                                                                      Arial,
                                                                      Helvetica,
                                                                      sans-serif;
                                                                    font-size: 13px;
                                                                    font-weight: 500;
                                                                    font-variant-ligatures: normal;
                                                                    color: #181818;
                                                                    text-transform: uppercase;
                                                                    text-align: center;
                                                                    text-align-last: center;
                                                                  ">
                                                                <span style="
                                                                      text-transform: uppercase;
                                                                    ">M</span><span>Ø</span><span style="
                                                                      text-transform: uppercase;
                                                                    ">RE</span>
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation"
                                  style="width: 100%">
                                  <tr>
                                    <td class="pc-w620-spacing-0-0-0-0" valign="top"
                                      style="padding: 24px 32px 0px 32px">
                                      <table width="100%" border="0" cellpadding="0" cellspacing="0"
                                        role="presentation">
                                        <tr>
                                          <!--[if gte mso 9]>
                                              <td
                                                height="1"
                                                valign="top"
                                                style="
                                                  line-height: 1px;
                                                  font-size: 1px;
                                                  border-bottom: 1px solid
                                                    #000000;
                                                "
                                              >
                                                &nbsp;
                                              </td>
                                            <![endif]-->
                                          <!--[if !gte mso 9]><!-- -->
                                          <td height="1" valign="top" style="
                                                line-height: 1px;
                                                font-size: 1px;
                                                border-bottom: 1px solid #000000;
                                              ">
                                            &nbsp;
                                          </td>
                                          <!--<![endif]-->
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <!-- END MODULE: Menu -->
                  </td>
                </tr>
                <tr>
                  <td valign="top">
                    <!-- BEGIN MODULE: Exhibition -->
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                      <tr>
                        <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px">
                          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation" style="
                                border-collapse: separate;
                                border-spacing: 0px;
                              ">
                            <tr>
                              <td valign="top" class="pc-w620-padding-24-24-48-24" style="
                                    padding: 48px 24px 48px 24px;
                                    border-radius: 0px;
                                    background-color: #ffffff;
                                    box-shadow: 10px 10px 0px 0px
                                      rgba(236, 234, 232, 1);
                                  " bgcolor="#ffffff">
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" valign="top" style="padding: 0px 0px 0px 0px">
                                      <img src="https://cloudfilesdm.com/postcards/image-1720275868746.jpg"
                                        class="pc-w620-width-78pc pc-w620-height-auto" width="469" height="auto"
                                        alt="GTX logo" style="
                                            display: block;
                                            border: 0;
                                            outline: 0;
                                            line-height: 100%;
                                            -ms-interpolation-mode: bicubic;
                                            width: 85%;
                                            height: auto;
                                            border-radius: 480px 480px 480px
                                              480px;
                                          " />
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" valign="top" style="padding: 32px 0px 16px 0px">
                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"
                                        style="
                                            border-collapse: separate;
                                            border-spacing: 0;
                                            margin-right: auto;
                                            margin-left: auto;
                                          ">
                                        <tr>
                                          <td valign="top" align="center">
                                            <div class="pc-font-alt pc-w620-fontSize-40px pc-w620-lineHeight-40" style="
                                                  line-height: 100%;
                                                  letter-spacing: -1px;
                                                  font-family: 'Cinzel', Arial,
                                                    Helvetica, sans-serif;
                                                  font-size: 56px;
                                                  font-weight: normal;
                                                  font-variant-ligatures: normal;
                                                  color: #1b1b1b;
                                                  text-align: center;
                                                  text-align-last: center;
                                                ">
                                              <div>
                                                <span style="letter-spacing: -1px"
                                                  data-letter-spacing-original="-1">Welcome to gtx!</span>
                                              </div>
                                            </div>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td class="pc-w620-spacing-0-0-32-0" align="center" valign="top"
                                      style="padding: 0px 0px 26px 0px">
                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="80%"
                                        align="center" style="
                                            border-collapse: separate;
                                            border-spacing: 0;
                                            margin-right: auto;
                                            margin-left: auto;
                                          ">
                                        <tr>
                                          <td valign="top" class="pc-w620-padding-0-0-0-0" align="center">
                                            <div class="pc-font-alt pc-w620-fontSize-15px pc-w620-lineHeight-139pc"
                                              style="
                                                  line-height: 140%;
                                                  letter-spacing: -0px;
                                                  font-family: 'Poppins', Arial,
                                                    Helvetica, sans-serif;
                                                  font-size: 16px;
                                                  font-weight: normal;
                                                  font-variant-ligatures: normal;
                                                  color: #2d2d2f;
                                                  text-align: center;
                                                  text-align-last: center;
                                                ">
                                              <div>
                                                <span>We&#39;re thrilled to have
                                                  you join our digital asset
                                                  ecosystem. To get started,
                                                  please verify your email
                                                  address by clicking the
                                                  button below.</span>
                                              </div>
                                              <div><span>&#xFEFF;</span></div>
                                            </div>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <th valign="top" align="center" style="
                                          padding: 0px 0px 0px 0px;
                                          text-align: center;
                                          font-weight: normal;
                                          line-height: 1;
                                        ">
                                      <!--[if mso]>
                                          <table
                                            border="0"
                                            cellpadding="0"
                                            cellspacing="0"
                                            role="presentation"
                                            align="center"
                                            style="
                                              border-collapse: separate;
                                              border-spacing: 0;
                                              margin-right: auto;
                                              margin-left: auto;
                                            "
                                          >
                                            <tr>
                                              <td
                                                valign="middle"
                                                align="center"
                                                style="
                                                  border-top: 1px solid #181818;
                                                  border-right: 1px solid
                                                    #181818;
                                                  border-bottom: 1px solid
                                                    #181818;
                                                  border-left: 1px solid #181818;
                                                  background-color: #ffffff;
                                                  text-align: center;
                                                  color: #ffffff;
                                                  padding: 12px 40px 12px 40px;
                                                  mso-padding-left-alt: 0;
                                                  margin-left: 40px;
                                                "
                                                bgcolor="#ffffff"
                                              >
                                                <a
                                                  class="pc-font-alt"
                                                  style="
                                                    display: inline-block;
                                                    text-decoration: none;
                                                    font-variant-ligatures: normal;
                                                    font-family: 'Poppins',
                                                      Arial, Helvetica,
                                                      sans-serif;
                                                    font-weight: 500;
                                                    font-size: 14px;
                                                    line-height: 24px;
                                                    letter-spacing: 0.04em;
                                                    text-align: center;
                                                    color: #181818;
                                                  "
                                                  href="{ verification_link }"
                                                  ><span style="display: block"
                                                    ><span
                                                      >VERIFY EMAIL</span
                                                    ></span
                                                  ></a
                                                >
                                              </td>
                                            </tr>
                                          </table>
                                        <![endif]-->
                                      <!--[if !mso]><!-- -->
                                      <a style="
                                            display: inline-block;
                                            box-sizing: border-box;
                                            border-top: 1px solid #181818;
                                            border-right: 1px solid #181818;
                                            border-bottom: 1px solid #181818;
                                            border-left: 1px solid #181818;
                                            background-color: #ffffff;
                                            padding: 12px 40px 12px 40px;
                                            font-family: 'Poppins', Arial,
                                              Helvetica, sans-serif;
                                            font-weight: 500;
                                            font-size: 14px;
                                            line-height: 24px;
                                            letter-spacing: 0.04em;
                                            color: #181818;
                                            vertical-align: top;
                                            text-align: center;
                                            text-align-last: center;
                                            text-decoration: none;
                                            -webkit-text-size-adjust: none;
                                            mso-hide: all;
                                          " href="{ verification_link }"><span style="display: block"><span>VERIFY
                                            EMAIL</span></span></a>
                                      <!--<![endif]-->
                                    </th>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <!-- END MODULE: Exhibition -->
                  </td>
                </tr>
                <tr>
                  <td valign="top">
                    <!-- BEGIN MODULE: Footer -->
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                      <tr>
                        <td class="pc-w620-spacing-0-0-0-0" style="padding: 0px 0px 0px 0px">
                          <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation" style="
                                border-collapse: separate;
                                border-spacing: 0px;
                              ">
                            <tr>
                              <td valign="top" class="pc-w620-padding-30-24-30-24" style="
                                    padding: 40px 32px 48px 32px;
                                    border-top: 24px solid #aab2bb00;
                                    border-right: 24px solid #aab2bb00;
                                    border-bottom: 24px solid #aab2bb00;
                                    border-left: 24px solid #aab2bb00;
                                    background-color: #aab2bb;
                                    box-shadow: 10px 10px 0px 0px
                                      rgba(236, 234, 232, 1);
                                  " bgcolor="#aab2bb">
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" valign="top" style="padding: 0px 0px 32px 0px">
                                      <img src="https://cloudfilesdm.com/postcards/image-1720272421793.png" class=""
                                        width="100" height="75" alt="GTX" style="
                                            display: block;
                                            border: 0;
                                            outline: 0;
                                            line-height: 100%;
                                            -ms-interpolation-mode: bicubic;
                                            width: 100px;
                                            height: auto;
                                            max-width: 100%;
                                          " />
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" style="padding: 0px 0px 27px 0px">
                                      <table class="pc-width-hug pc-w620-gridCollapsed-0" align="center" border="0"
                                        cellpadding="0" cellspacing="0" role="presentation">
                                        <tr class="pc-grid-tr-first pc-grid-tr-last">
                                          <td class="pc-grid-td-first pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation" align="center" style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            ">
                                                          <tr>
                                                            <td valign="top" align="center" style="
                                                                  padding: 0px
                                                                    0px 0px 0px;
                                                                ">
                                                              <a class="pc-font-alt pc-w620-fontSize-13px"
                                                                href="https://www.gtx.com.co/" target="_blank" style="
                                                                    text-decoration: none;
                                                                    line-height: 140%;
                                                                    letter-spacing: 0.06em;
                                                                    font-family: 'Poppins',
                                                                      Arial,
                                                                      Helvetica,
                                                                      sans-serif;
                                                                    font-size: 14px;
                                                                    font-weight: 500;
                                                                    font-variant-ligatures: normal;
                                                                    color: #f9eae7;
                                                                    text-transform: uppercase;
                                                                    text-align: center;
                                                                    text-align-last: center;
                                                                  ">
                                                                <span style="
                                                                      text-transform: uppercase;
                                                                    ">H<span>Ø</span><span style="
                                                                      text-transform: uppercase;
                                                                    ">ME</span>
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td class="pc-w620-spacing-0-0-0-0" valign="top">
                                                              <table border="0" cellpadding="0" cellspacing="0"
                                                                role="presentation" width="100%" style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  ">
                                                                <tr>
                                                                  <td valign="top"
                                                                    class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                    align="center" style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      ">
                                                                    <a class="pc-font-alt pc-w620-textAlign-center pc-w620-fontSize-13px"
                                                                      href="https://www.gtx.com.co/news" target="_blank"
                                                                      style="
                                                                          text-decoration: none;
                                                                          line-height: 140%;
                                                                          letter-spacing: 0.06em;
                                                                          font-family: 'Poppins',
                                                                            Arial,
                                                                            Helvetica,
                                                                            sans-serif;
                                                                          font-size: 14px;
                                                                          font-weight: 500;
                                                                          font-variant-ligatures: normal;
                                                                          color: #f9eae7;
                                                                          text-transform: uppercase;
                                                                          text-align: center;
                                                                          text-align-last: center;
                                                                        ">
                                                                      <span style="
                                                                            text-transform: uppercase;
                                                                          ">NEWS</span>
                                                                    </a>
                                                                  </td>
                                                                </tr>
                                                              </table>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td class="pc-w620-spacing-0-0-0-0" valign="top">
                                                              <table border="0" cellpadding="0" cellspacing="0"
                                                                role="presentation" width="100%" style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  ">
                                                                <tr>
                                                                  <td valign="top"
                                                                    class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                    align="center" style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      ">
                                                                    <a class="pc-font-alt pc-w620-textAlign-center pc-w620-fontSize-13px"
                                                                      href="https://www.gtx.com.co/#about"
                                                                      target="_blank" style="
                                                                          text-decoration: none;
                                                                          line-height: 140%;
                                                                          letter-spacing: 0.06em;
                                                                          font-family: 'Poppins',
                                                                            Arial,
                                                                            Helvetica,
                                                                            sans-serif;
                                                                          font-size: 14px;
                                                                          font-weight: 500;
                                                                          font-variant-ligatures: normal;
                                                                          color: #f9eae7;
                                                                          text-transform: uppercase;
                                                                          text-align: center;
                                                                          text-align-last: center;
                                                                        ">
                                                                      <span>Ø</span><span style="
                                                                            text-transform: uppercase;
                                                                          ">UR
                                                                        ST</span><span>Ø</span><span style="
                                                                            text-transform: uppercase;
                                                                          ">RY</span>
                                                                    </a>
                                                                  </td>
                                                                </tr>
                                                              </table>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td class="pc-w620-spacing-0-0-0-0" valign="top">
                                                              <table border="0" cellpadding="0" cellspacing="0"
                                                                role="presentation" width="100%" style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  ">
                                                                <tr>
                                                                  <td valign="top"
                                                                    class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                    align="center" style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      ">
                                                                    <a class="pc-font-alt pc-w620-textAlign-center pc-w620-fontSize-13px"
                                                                      href="mailto:info@gtx.com.co" target="_blank"
                                                                      style="
                                                                          text-decoration: none;
                                                                          line-height: 140%;
                                                                          letter-spacing: 0.06em;
                                                                          font-family: 'Poppins',
                                                                            Arial,
                                                                            Helvetica,
                                                                            sans-serif;
                                                                          font-size: 14px;
                                                                          font-weight: 500;
                                                                          font-variant-ligatures: normal;
                                                                          color: #f9eae7;
                                                                          text-transform: uppercase;
                                                                          text-align: center;
                                                                          text-align-last: center;
                                                                        ">
                                                                      <span>SUPPØ</span><span style="
                                                                            text-transform: uppercase;
                                                                          ">RT</span>
                                                                    </a>
                                                                  </td>
                                                                </tr>
                                                              </table>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-grid-td-last pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              ">
                                            <table class="pc-w620-width-hug" border="0" cellpadding="0" cellspacing="0"
                                              role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td class="pc-w620-padding-0-0-0-0" align="center" valign="middle"
                                                  style="
                                                      padding: 0px 0px 0px 0px;
                                                    ">
                                                  <table class="pc-w620-width-hug" align="center" border="0"
                                                    cellpadding="0" cellspacing="0" role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation" align="center" style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            ">
                                                          <tr>
                                                            <td valign="top" align="center">
                                                              <a class="pc-font-alt pc-w620-fontSize-13px"
                                                                href="https://www.gtx.com.co/" target="_blank" style="
                                                                    text-decoration: none;
                                                                    line-height: 140%;
                                                                    letter-spacing: 0.06em;
                                                                    font-family: 'Poppins',
                                                                      Arial,
                                                                      Helvetica,
                                                                      sans-serif;
                                                                    font-size: 14px;
                                                                    font-weight: 500;
                                                                    font-variant-ligatures: normal;
                                                                    color: #f9eae7;
                                                                    text-transform: uppercase;
                                                                    text-align: center;
                                                                    text-align-last: center;
                                                                  ">
                                                                <span style="
                                                                      text-transform: uppercase;
                                                                    ">FAQ</span>
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation"
                                  style="width: 100%">
                                  <tr>
                                    <td valign="top" style="padding: 0px 0px 32px 0px">
                                      <table class="pc-w620-width-270" width="300" border="0" cellpadding="0"
                                        cellspacing="0" role="presentation" style="margin: auto">
                                        <tr>
                                          <!--[if gte mso 9]>
                                              <td
                                                height="1"
                                                valign="top"
                                                style="
                                                  line-height: 1px;
                                                  font-size: 1px;
                                                  border-bottom: 1px solid
                                                    #e6e4e2;
                                                "
                                              >
                                                &nbsp;
                                              </td>
                                            <![endif]-->
                                          <!--[if !gte mso 9]><!-- -->
                                          <td height="1" valign="top" style="
                                                line-height: 1px;
                                                font-size: 1px;
                                                border-bottom: 1px solid #e6e4e2;
                                              ">
                                            &nbsp;
                                          </td>
                                          <!--<![endif]-->
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" style="padding: 0px 0px 28px 0px">
                                      <table class="pc-width-hug pc-w620-gridCollapsed-0" align="center" border="0"
                                        cellpadding="0" cellspacing="0" role="presentation">
                                        <tr class="pc-grid-tr-first pc-grid-tr-last">
                                          <td class="pc-grid-td-first pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td align="center" valign="middle">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td valign="top">
                                                              <a href="https://www.linkedin.com/company/gtxdotcom/"
                                                                target="_blank">
                                                                <img
                                                                  src="https://cloudfilesdm.com/postcards/f94094decb82ff5c929413bce4a4b231.png"
                                                                  class="" width="20" height="20" style="
                                                                    display: block;
                                                                    border: 0;
                                                                    outline: 0;
                                                                    line-height: 100%;
                                                                    -ms-interpolation-mode: bicubic;
                                                                    width: 20px;
                                                                    height: 20px;
                                                                  " alt="linkedin" />
                                                              </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td align="center" valign="middle">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td valign="top">
                                                              <a href="https://x.com/gtxdotcom" target="_blank">
                                                              <img
                                                                src="https://cloudfilesdm.com/postcards/feea36d23d731ae10d42f7f5ef39f688.png"
                                                                class="" width="20" height="20" style="
                                                                    display: block;
                                                                    border: 0;
                                                                    outline: 0;
                                                                    line-height: 100%;
                                                                    -ms-interpolation-mode: bicubic;
                                                                    width: 20px;
                                                                    height: 20px;
                                                                  " alt="X" />
                                                                  </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td align="center" valign="middle">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td valign="top">
                                                              <a href="https://www.instagram.com/gtxdotcom/" target="_blank">
                                                              <img
                                                                src="https://cloudfilesdm.com/postcards/b01bc93061ef80b1e939305054c5ad54.png"
                                                                class="" width="20" height="20" style="
                                                                    display: block;
                                                                    border: 0;
                                                                    outline: 0;
                                                                    line-height: 100%;
                                                                    -ms-interpolation-mode: bicubic;
                                                                    width: 20px;
                                                                    height: 20px;
                                                                  " alt="instagram" />
                                                                  </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td align="center" valign="middle">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td valign="top">
                                                              <a href="https://web.facebook.com/profile.php?id=100094228042198&_rdc=1&_rdr" target="_blank">
                                                              <img
                                                                src="https://cloudfilesdm.com/postcards/cb439f420516f1ce61606aace4de6a16.png"
                                                                class="" width="20" height="20" style="
                                                                    display: block;
                                                                    border: 0;
                                                                    outline: 0;
                                                                    line-height: 100%;
                                                                    -ms-interpolation-mode: bicubic;
                                                                    width: 20px;
                                                                    height: 20px;
                                                                  " alt="facebook" />
                                                                  </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                          <td class="pc-grid-td-last pc-w620-itemsSpacings-20-0" valign="middle" style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              ">
                                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                ">
                                              <tr>
                                                <td align="center" valign="middle">
                                                  <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                    role="presentation">
                                                    <tr>
                                                      <td align="center" valign="top">
                                                        <table align="center" border="0" cellpadding="0" cellspacing="0"
                                                          role="presentation">
                                                          <tr>
                                                            <td valign="top">
                                                              <a href="https://discord.com/invite/dVmMCdf9jx" target="_blank">
                                                              <img
                                                                src="https://cloudfilesdm.com/postcards/5bfd2f3194f11fbe40227a1539600a03.png"
                                                                class="" width="20" height="20" style="
                                                                    display: block;
                                                                    border: 0;
                                                                    outline: 0;
                                                                    line-height: 100%;
                                                                    -ms-interpolation-mode: bicubic;
                                                                    width: 20px;
                                                                    height: 20px;
                                                                  " alt="discord" />
                                                                  </a>
                                                            </td>
                                                          </tr>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </table>
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" valign="top" style="padding: 0px 20px 32px 20px">
                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"
                                        style="
                                            border-collapse: separate;
                                            border-spacing: 0;
                                            margin-right: auto;
                                            margin-left: auto;
                                          ">
                                        <tr>
                                          <td valign="top" align="center">
                                            <div class="pc-font-alt" style="
                                                  line-height: 140%;
                                                  letter-spacing: 0px;
                                                  font-family: 'Poppins', Arial,
                                                    Helvetica, sans-serif;
                                                  font-size: 14px;
                                                  font-weight: normal;
                                                  font-variant-ligatures: normal;
                                                  color: #ffffff99;
                                                  text-align: center;
                                                  text-align-last: center;
                                                ">
                                              <div>
                                                <span style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    ">Want to change which emails
                                                  you receive from us? You can
                                                  update your preferences </span><a
                                                  href="" target="_blank" style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "><span style="
                                                        text-decoration: underline;
                                                        font-weight: 400;
                                                        font-style: normal;
                                                      ">here</span></a><span style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    ">
                                                  or unsubscribe </span><a href=""
                                                  target="_blank" style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "><span style="
                                                        text-decoration: underline;
                                                        font-weight: 400;
                                                        font-style: normal;
                                                      ">here</span></a><span style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    ">. You can view our privacy
                                                  policy </span><a href=""
                                                  target="_blank" style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "><span style="
                                                        text-decoration: underline;
                                                        font-weight: 400;
                                                        font-style: normal;
                                                      ">here</span></a><span style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    ">.</span>
                                              </div>
                                            </div>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
                                  <tr>
                                    <td align="center" valign="top" style="padding: 0px 0px 0px 0px">
                                      <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"
                                        style="
                                            border-collapse: separate;
                                            border-spacing: 0;
                                            margin-right: auto;
                                            margin-left: auto;
                                          ">
                                        <tr>
                                          <td valign="top" align="center">
                                            <div class="pc-font-alt" style="
                                                  line-height: 140%;
                                                  letter-spacing: 0px;
                                                  font-family: 'Poppins', Arial,
                                                    Helvetica, sans-serif;
                                                  font-size: 14px;
                                                  font-weight: normal;
                                                  font-variant-ligatures: normal;
                                                  color: #ffffff99;
                                                  text-align: center;
                                                  text-align-last: center;
                                                ">
                                              <div>
                                                <span style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    ">© 2024</span><a href="https://www.gtx.com.co/" target="_blank"
                                                  style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "><span> GTX</span></a><span style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    ">. All Rights
                                                  Reserved.</span>
                                              </div>
                                            </div>
                                          </td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                    <!-- END MODULE: Footer -->
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
  <!-- Fix for Gmail on iOS -->
  <div class="pc-gmail-fix" style="white-space: nowrap; font: 15px courier; line-height: 0">
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
  </div>
</body>

</html>
        """
        send_email(email, "Welcome to GTX - Your Gateway to Digital Assets!", email_template)


        conn.execute(
            "INSERT INTO verification (user_id, token) VALUES (?, ?)", (user_id, token)
        )
        conn.commit()
        conn.close()

        return (
            jsonify(
                {"message": "User created successfully. Please verify your email."}
            ),
            201,
        )
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username or email already exists"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/verify/<token>", methods=["GET"])
def verify_email(token):
    try:
        payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        user_id = payload["sub"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if user:
            conn.execute(
                "UPDATE users SET is_verified = ? WHERE id = ?", (True, user_id)
            )
            conn.execute("DELETE FROM verification WHERE user_id = ?", (user_id,))
            conn.commit()
            conn.close()
            return "Email verified successfully!"
        else:
            return "Invalid verification token.", 400
    except jwt.ExpiredSignatureError:
        return "Verification link expired. Please sign up again.", 400
    except jwt.InvalidTokenError:
        return "Invalid verification token.", 400
    except Exception as e:
        return str(e), 500


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    try:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()
        if user and check_password_hash(user["password"], password):
            if not user["is_verified"]:
                return (
                    jsonify({"message": "Please verify your email before logging in."}),
                    403,
                )

            # Exclude password from the user details
            user_details = dict(user)
            del user_details["password"]

            token = jwt.encode(
                {
                    "user_id": user["id"],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                },
                app.config["SECRET_KEY"],
                algorithm="HS256",
            )

            return jsonify({"token": token, "user": user_details}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    if not data or "email" not in data:
        return jsonify({"error": "No email provided"}), 400

    email = data["email"]
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO notification (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()
        result = {
            "message": "Email registered for product launch notifications",
            "email": email,
        }
        return jsonify(result), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/newsletter", methods=["POST"])
def newsletter():
    data = request.get_json()
    if not data or "email" not in data:
        return jsonify({"error": "No email provided"}), 400

    email = data["email"]
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO newsletter (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()
        result = {"message": "Email registered for newsletter", "email": email}
        return jsonify(result), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/emails", methods=["GET"])
def get_emails():
    try:
        conn = get_db_connection()
        notification_emails = conn.execute("SELECT * FROM notification").fetchall()
        newsletter_emails = conn.execute("SELECT * FROM newsletter").fetchall()
        conn.close()

        # Convert rows to list of dictionaries
        notification_emails = [dict(row) for row in notification_emails]
        newsletter_emails = [dict(row) for row in newsletter_emails]

        result = {
            "message": "Registered emails retrieved successfully",
            "notification_emails": notification_emails,
            "newsletter_emails": newsletter_emails,
        }
        return jsonify(result), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/emails/notification", methods=["GET"])
def get_notification_emails():
    try:
        conn = get_db_connection()
        notification_emails = conn.execute("SELECT * FROM notification").fetchall()
        conn.close()

        # Convert rows to list of dictionaries
        notification_emails = [dict(row) for row in notification_emails]

        result = {
            "message": "Notification emails retrieved successfully",
            "notification_emails": notification_emails,
        }
        return jsonify(result), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/emails/newsletter", methods=["GET"])
def get_newsletter_emails():
    try:
        conn = get_db_connection()
        newsletter_emails = conn.execute("SELECT * FROM newsletter").fetchall()
        conn.close()

        # Convert rows to list of dictionaries
        newsletter_emails = [dict(row) for row in newsletter_emails]

        result = {
            "message": "Newsletter emails retrieved successfully",
            "newsletter_emails": newsletter_emails,
        }
        return jsonify(result), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run()
