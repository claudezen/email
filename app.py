from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Email configuration
app.config["MAIL_SERVER"] = "libra.vivawebhost.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "no-reply@assetra.xyz"
app.config["MAIL_PASSWORD"] = "B;Er2x&o$cY]"
app.config["MAIL_DEFAULT_SENDER"] = "no-reply@assetra.xyz"

mail = Mail(app)


def generate_email_content(code):
    return f"""
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

  <body
    class="body pc-font-alt"
    style="
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
    "
    bgcolor="#fbf4ee"
  >
    <table
      class="pc-project-body"
      style="table-layout: fixed; min-width: 600px; background-color: #fbf4ee"
      bgcolor="#fbf4ee"
      width="100%"
      border="0"
      cellspacing="0"
      cellpadding="0"
      role="presentation"
    >
      <tr>
        <td align="center" valign="top">
          <table
            class="pc-project-container"
            align="center"
            width="600"
            style="width: 600px; max-width: 600px"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
          >
            <tr>
              <td
                class="pc-w620-padding-0-0-0-0"
                style="padding: 20px 0px 20px 0px"
                align="left"
                valign="top"
              >
                <table
                  border="0"
                  cellpadding="0"
                  cellspacing="0"
                  role="presentation"
                  width="100%"
                  style="width: 100%"
                >
                  <tr>
                    <td valign="top">
                      <!-- BEGIN MODULE: Menu -->
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        role="presentation"
                      >
                        <tr>
                          <td
                            class="pc-w620-spacing-0-0-0-0"
                            style="padding: 0px 0px 0px 0px"
                          >
                            <table
                              width="100%"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              role="presentation"
                              style="
                                border-collapse: separate;
                                border-spacing: 0px;
                              "
                            >
                              <tr>
                                <td
                                  valign="top"
                                  class="pc-w620-padding-8-24-24-24"
                                  style="
                                    padding: 48px 24px 0px 24px;
                                    border-radius: 0px;
                                    background-color: #ebddcc;
                                  "
                                  bgcolor="#ebddcc"
                                >
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        class="pc-w620-spacing-24-0-24-0"
                                        align="center"
                                        valign="top"
                                        style="padding: 0px 0px 24px 0px"
                                      >
                                        <img
                                          src="https://cloudfilesdm.com/postcards/image-1726312612410.png"
                                          class="pc-w620-width-100 pc-w620-height-auto"
                                          width="120"
                                          height="29"
                                          alt=""
                                          style="
                                            display: block;
                                            outline: 0;
                                            line-height: 100%;
                                            -ms-interpolation-mode: bicubic;
                                            width: 120px;
                                            height: auto;
                                            max-width: 100%;
                                            border: 0;
                                          "
                                        />
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        class="pc-w620-spacing-0-0-24-0"
                                        align="center"
                                        style="padding: 0px 0px 0px 0px"
                                      >
                                        <table
                                          class="pc-width-hug pc-w620-gridCollapsed-0 pc-w620-width-hug"
                                          align="center"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                        >
                                          <tr
                                            class="pc-grid-tr-first pc-grid-tr-last"
                                          >
                                            <td
                                              class="pc-grid-td-first pc-w620-itemsSpacings-18-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="left"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="left"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="left"
                                                          valign="top"
                                                        >
                                                          <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            align="left"
                                                            style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            "
                                                          >
                                                            <tr>
                                                              <td
                                                                valign="top"
                                                                align="left"
                                                              >
                                                                <div
                                                                  class="pc-font-alt"
                                                                  style="
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
                                                                  "
                                                                >
                                                                  <div>
                                                                    <span
                                                                      >&#xFEFF;</span
                                                                    ><a
                                                                      href="https://www.assetra.xyz/"
                                                                      target="_blank"
                                                                      style="
                                                                        text-decoration: none;
                                                                        color: #181818;
                                                                      "
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >H</span
                                                                      ><span
                                                                        >Ø</span
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >ME</span
                                                                      ></a
                                                                    ><span
                                                                      >&#xFEFF;</span
                                                                    >
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
                                            <td
                                              class="pc-w620-itemsSpacings-18-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td
                                                                class="pc-w620-spacing-0-0-0-0"
                                                                valign="top"
                                                              >
                                                                <table
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  width="100%"
                                                                  style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <td
                                                                      valign="top"
                                                                      class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                      align="center"
                                                                      style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      "
                                                                    >
                                                                      <div
                                                                        class="pc-font-alt pc-w620-textAlign-center"
                                                                        style="
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
                                                                        "
                                                                      >
                                                                        <div>
                                                                          <span
                                                                            >&#xFEFF;</span
                                                                          ><a
                                                                            href="https://www.assetra.xyz/#about"
                                                                            target="_blank"
                                                                            style="
                                                                              text-decoration: none;
                                                                              color: #181818;
                                                                            "
                                                                            ><span
                                                                              style="
                                                                                text-transform: uppercase;
                                                                              "
                                                                              >AB</span
                                                                            ><span
                                                                              >Ø</span
                                                                            ><span
                                                                              style="
                                                                                text-transform: uppercase;
                                                                              "
                                                                              >UT
                                                                              US</span
                                                                            ></a
                                                                          ><span
                                                                            >&#xFEFF;</span
                                                                          >
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
                                            </td>
                                            <td
                                              class="pc-w620-itemsSpacings-18-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            align="center"
                                                            style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            "
                                                          >
                                                            <tr>
                                                              <td
                                                                valign="top"
                                                                align="center"
                                                              >
                                                                <div
                                                                  class="pc-font-alt"
                                                                  style="
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
                                                                  "
                                                                >
                                                                  <div>
                                                                    <span
                                                                      >&#xFEFF;</span
                                                                    ><a
                                                                      href="mailto:support@assetra.xyz"
                                                                      target="_blank"
                                                                      style="
                                                                        text-decoration: none;
                                                                        color: #181818;
                                                                      "
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >SUPP</span
                                                                      ><span
                                                                        >Ø</span
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >RT</span
                                                                      ></a
                                                                    ><span
                                                                      >&#xFEFF;</span
                                                                    >
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
                                            <td
                                              class="pc-w620-itemsSpacings-18-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            align="center"
                                                            style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            "
                                                          >
                                                            <tr>
                                                              <td
                                                                valign="top"
                                                                align="center"
                                                              >
                                                                <div
                                                                  class="pc-font-alt"
                                                                  style="
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
                                                                  "
                                                                >
                                                                  <div>
                                                                    <span
                                                                      >﻿</span
                                                                    ><a
                                                                      href="https://www.assetra.xyz/blog"
                                                                      target="_blank"
                                                                      style="
                                                                        text-decoration: none;
                                                                        color: #181818;
                                                                      "
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >B</span
                                                                      ></a
                                                                    ><span
                                                                      style="
                                                                        text-transform: uppercase;
                                                                      "
                                                                      >l</span
                                                                    ><a
                                                                      href="https://www.assetra.xyz/blog"
                                                                      target="_blank"
                                                                      style="
                                                                        text-decoration: none;
                                                                        color: #181818;
                                                                      "
                                                                      ><span
                                                                        >Øg</span
                                                                      ></a
                                                                    ><span
                                                                      >&#xFEFF;</span
                                                                    >
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
                                            <td
                                              class="pc-grid-td-last pc-w620-itemsSpacings-18-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            align="center"
                                                            style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            "
                                                          >
                                                            <tr>
                                                              <td
                                                                valign="top"
                                                                align="center"
                                                              >
                                                                <div
                                                                  class="pc-font-alt"
                                                                  style="
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
                                                                  "
                                                                >
                                                                  <div>
                                                                    <span
                                                                      style="
                                                                        text-transform: uppercase;
                                                                      "
                                                                      >f</span
                                                                    ><a
                                                                      href="https://www.assetra.xyz/forum"
                                                                      target="_blank"
                                                                      style="
                                                                        text-decoration: none;
                                                                        color: #181818;
                                                                      "
                                                                      ><span
                                                                        >Ø</span
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >Rum</span
                                                                      ></a
                                                                    ><span
                                                                      >﻿</span
                                                                    >
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
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                    style="width: 100%"
                                  >
                                    <tr>
                                      <td
                                        class="pc-w620-spacing-0-0-0-0"
                                        valign="top"
                                        style="padding: 24px 32px 0px 32px"
                                      >
                                        <table
                                          width="100%"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                        >
                                          <tr>
                                            <!--[if gte mso 9]>
                                              <td
                                                height="1"
                                                valign="top"
                                                style="
                                                  line-height: 1px;
                                                  font-size: 1px;
                                                  border-bottom: 1px solid
                                                    #cfbfac;
                                                "
                                              >
                                                &nbsp;
                                              </td>
                                            <![endif]-->
                                            <!--[if !gte mso 9]><!-- -->
                                            <td
                                              height="1"
                                              valign="top"
                                              style="
                                                line-height: 1px;
                                                font-size: 1px;
                                                border-bottom: 1px solid #cfbfac;
                                              "
                                            >
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
                      <!-- BEGIN MODULE: Blog -->
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        role="presentation"
                      >
                        <tr>
                          <td
                            class="pc-w620-spacing-0-0-0-0"
                            style="padding: 0px 0px 0px 0px"
                          >
                            <table
                              width="100%"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              role="presentation"
                              style="
                                border-collapse: separate;
                                border-spacing: 0px;
                              "
                            >
                              <tr>
                                <td
                                  valign="top"
                                  class="pc-w620-padding-32-24-24-24"
                                  style="
                                    padding: 24px 24px 24px 24px;
                                    border-right: 24px solid #ecddd0;
                                    border-left: 24px solid #ecddd0;
                                    background-color: #ffffff;
                                  "
                                  bgcolor="#ffffff"
                                >
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td style="padding: 16px 0px 16px 0px">
                                        <table
                                          class="pc-width-fill pc-w620-gridCollapsed-1 pc-w620-width-fill pc-w620-dir-rtl"
                                          width="100%"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                        >
                                          <tr
                                            class="pc-grid-tr-first pc-grid-tr-last"
                                          >
                                            <td
                                              class="pc-grid-td-first pc-w620-itemsSpacings-0-16"
                                              align="center"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                  width: 130px;
                                                "
                                                width="130"
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="left"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="left"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="left"
                                                          valign="top"
                                                        >
                                                          <table
                                                            width="100%"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            style="width: 100%"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <table
                                                                  class="pc-w620-width-120"
                                                                  width="100%"
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  style="
                                                                    margin-right: auto;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <!--[if gte mso 9]>
                                                                      <td
                                                                        height="1"
                                                                        valign="top"
                                                                        style="
                                                                          line-height: 1px;
                                                                          font-size: 1px;
                                                                          border-bottom: 1px
                                                                            solid
                                                                            #33333366;
                                                                        "
                                                                      >
                                                                        &nbsp;
                                                                      </td>
                                                                    <![endif]-->
                                                                    <!--[if !gte mso 9]><!-- -->
                                                                    <td
                                                                      height="1"
                                                                      valign="top"
                                                                      style="
                                                                        line-height: 1px;
                                                                        font-size: 1px;
                                                                        border-bottom: 1px
                                                                          solid
                                                                          #33333366;
                                                                      "
                                                                    >
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
                                            </td>
                                            <td
                                              class="pc-w620-itemsSpacings-0-16"
                                              align="center"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                  width: 100%;
                                                "
                                                width="100%"
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="left"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="left"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="left"
                                                          valign="top"
                                                        >
                                                          <table
                                                            width="100%"
                                                            align="left"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <table
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  width="100%"
                                                                  align="center"
                                                                  style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <td
                                                                      valign="top"
                                                                      align="center"
                                                                    >
                                                                      <div
                                                                        class="pc-font-alt"
                                                                        style="
                                                                          line-height: 120%;
                                                                          letter-spacing: 2px;
                                                                          font-family: 'Poppins',
                                                                            Arial,
                                                                            Helvetica,
                                                                            sans-serif;
                                                                          font-size: 14px;
                                                                          font-weight: normal;
                                                                          font-variant-ligatures: normal;
                                                                          color: #333333;
                                                                          text-transform: uppercase;
                                                                          text-align: center;
                                                                          text-align-last: center;
                                                                        "
                                                                      >
                                                                        <div>
                                                                          <span
                                                                            >The
                                                                            New
                                                                            FrØntier</span
                                                                          >
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
                                            </td>
                                            <td
                                              class="pc-grid-td-last pc-w620-itemsSpacings-0-16"
                                              align="center"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                  width: 130px;
                                                "
                                                width="130"
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="left"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="left"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="left"
                                                          valign="top"
                                                        >
                                                          <table
                                                            width="100%"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            style="width: 100%"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <table
                                                                  class="pc-w620-width-120"
                                                                  width="100%"
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  style="
                                                                    margin-right: auto;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <!--[if gte mso 9]>
                                                                      <td
                                                                        height="1"
                                                                        valign="top"
                                                                        style="
                                                                          line-height: 1px;
                                                                          font-size: 1px;
                                                                          border-bottom: 1px
                                                                            solid
                                                                            #33333366;
                                                                        "
                                                                      >
                                                                        &nbsp;
                                                                      </td>
                                                                    <![endif]-->
                                                                    <!--[if !gte mso 9]><!-- -->
                                                                    <td
                                                                      height="1"
                                                                      valign="top"
                                                                      style="
                                                                        line-height: 1px;
                                                                        font-size: 1px;
                                                                        border-bottom: 1px
                                                                          solid
                                                                          #33333366;
                                                                      "
                                                                    >
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
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        class="pc-w620-spacing-0-0-16-0"
                                        align="center"
                                        valign="top"
                                        style="padding: 0px 0px 16px 0px"
                                      >
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          width="100%"
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
                                              valign="top"
                                              class="pc-w620-padding-0-0-0-0"
                                              align="center"
                                            >
                                              <div
                                                class="pc-font-alt pc-w620-fontSize-40px"
                                                style="
                                                  line-height: 120%;
                                                  letter-spacing: -1px;
                                                  font-family: 'Cinzel', Arial,
                                                    Helvetica, sans-serif;
                                                  font-size: 56px;
                                                  font-weight: normal;
                                                  font-variant-ligatures: normal;
                                                  color: #181818;
                                                  text-align: center;
                                                  text-align-last: center;
                                                "
                                              >
                                                <div><span>Welcøme!</span></div>
                                              </div>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        class="pc-w620-spacing-0-0-24-0"
                                        align="center"
                                        valign="top"
                                        style="padding: 0px 24px 32px 24px"
                                      >
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          width="80%"
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
                                              valign="top"
                                              class="pc-w620-padding-0-0-0-0"
                                              align="center"
                                            >
                                              <div
                                                class="pc-font-alt pc-w620-fontSize-15px pc-w620-lineHeight-139pc"
                                                style="
                                                  line-height: 140%;
                                                  letter-spacing: -0px;
                                                  font-family: 'Poppins', Arial,
                                                    Helvetica, sans-serif;
                                                  font-size: 16px;
                                                  font-weight: normal;
                                                  font-variant-ligatures: normal;
                                                  color: #333333;
                                                  text-align: center;
                                                  text-align-last: center;
                                                "
                                              >
                                                <div>
                                                  <span
                                                    >You&#39;re about to embark
                                                    on a transformative journey,
                                                    where digital assets meet
                                                    limitless possibilities.
                                                    We&#39;re excited to have
                                                    you with us as we redefine
                                                    the future of finance and
                                                    empower you to thrive in
                                                    this new era.</span
                                                  >
                                                </div>
                                                <div>
                                                  <span>﻿<br /></span
                                                  ><span style="font-size: 14px"
                                                    >To unlock your access and
                                                    begin your journey, please
                                                    verify your email by using
                                                    the code below.</span
                                                  >
                                                </div>
                                              </div>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <th
                                        valign="top"
                                        align="center"
                                        style="
                                          padding: 0px 0px 32px 0px;
                                          text-align: center;
                                          font-weight: normal;
                                          line-height: 1;
                                        "
                                      >
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
                                                  ><span style="display: block"
                                                    ><span>{ code }</span></span
                                                  ></a
                                                >
                                              </td>
                                            </tr>
                                          </table>
                                        <![endif]-->
                                        <!--[if !mso]><!-- -->
                                        <a
                                          style="
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
                                          "
                                          ><span style="display: block"
                                            ><span>{ code }</span></span
                                          ></a
                                        >
                                        <!--<![endif]-->
                                      </th>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td valign="top">
                                        <img
                                          src="https://cloudfilesdm.com/postcards/image-1726312611306.jpg"
                                          class=""
                                          width="504"
                                          height="auto"
                                          alt=""
                                          style="
                                            display: block;
                                            outline: 0;
                                            line-height: 100%;
                                            -ms-interpolation-mode: bicubic;
                                            width: 100%;
                                            height: auto;
                                            border-radius: 500px 0px 0px 0px;
                                            border: 0;
                                          "
                                        />
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                      <!-- END MODULE: Blog -->
                    </td>
                  </tr>
                  <tr>
                    <td valign="top">
                      <!-- BEGIN MODULE: Footer -->
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        role="presentation"
                      >
                        <tr>
                          <td
                            class="pc-w620-spacing-0-0-0-0"
                            style="padding: 0px 0px 0px 0px"
                          >
                            <table
                              width="100%"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              role="presentation"
                              style="
                                border-collapse: separate;
                                border-spacing: 0px;
                              "
                            >
                              <tr>
                                <td
                                  valign="top"
                                  class="pc-w620-padding-30-24-30-24"
                                  style="
                                    padding: 40px 32px 48px 32px;
                                    border-top: 24px solid #ecddd0;
                                    border-right: 24px solid #ecddd0;
                                    border-bottom: 24px solid #ecddd0;
                                    border-left: 24px solid #ecddd0;
                                    background-color: #8b5549;
                                  "
                                  bgcolor="#8b5549"
                                >
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        align="center"
                                        valign="top"
                                        style="padding: 0px 0px 32px 0px"
                                      >
                                        <img
                                          src="https://cloudfilesdm.com/postcards/image-1726312613507.png"
                                          class=""
                                          width="100"
                                          height="24"
                                          alt=""
                                          style="
                                            display: block;
                                            outline: 0;
                                            line-height: 100%;
                                            -ms-interpolation-mode: bicubic;
                                            width: 100px;
                                            height: auto;
                                            max-width: 100%;
                                            border: 0;
                                          "
                                        />
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        align="center"
                                        style="padding: 0px 0px 27px 0px"
                                      >
                                        <table
                                          class="pc-width-hug pc-w620-gridCollapsed-0"
                                          align="center"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                        >
                                          <tr
                                            class="pc-grid-tr-first pc-grid-tr-last"
                                          >
                                            <td
                                              class="pc-grid-td-first pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            align="center"
                                                            style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            "
                                                          >
                                                            <tr>
                                                              <td
                                                                valign="top"
                                                                align="center"
                                                                style="
                                                                  padding: 0px
                                                                    0px 0px 0px;
                                                                "
                                                              >
                                                                <div
                                                                  class="pc-font-alt pc-w620-fontSize-13px"
                                                                  style="
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
                                                                  "
                                                                >
                                                                  <div>
                                                                    <span
                                                                      >&#xFEFF;</span
                                                                    ><a
                                                                      href="https://www.assetra.xyz/"
                                                                      target="_blank"
                                                                      style="
                                                                        text-decoration: none;
                                                                        color: #f9eae7;
                                                                      "
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >H</span
                                                                      ><span
                                                                        >Ø</span
                                                                      ><span
                                                                        style="
                                                                          text-transform: uppercase;
                                                                        "
                                                                        >ME</span
                                                                      ></a
                                                                    ><span
                                                                      >&#xFEFF;</span
                                                                    >
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
                                            <td
                                              class="pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td
                                                                class="pc-w620-spacing-0-0-0-0"
                                                                valign="top"
                                                              >
                                                                <table
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  width="100%"
                                                                  style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <td
                                                                      valign="top"
                                                                      class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                      align="center"
                                                                      style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      "
                                                                    >
                                                                      <div
                                                                        class="pc-font-alt pc-w620-textAlign-center pc-w620-fontSize-13px"
                                                                        style="
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
                                                                        "
                                                                      >
                                                                        <div>
                                                                          <span
                                                                            >﻿</span
                                                                          ><a
                                                                            href="https://www.assetra.xyz/blog"
                                                                            target="_blank"
                                                                            style="
                                                                              text-decoration: none;
                                                                              color: #f9eae7;
                                                                            "
                                                                            ><span
                                                                              style="
                                                                                text-transform: uppercase;
                                                                              "
                                                                              >B</span
                                                                            ></a
                                                                          ><span
                                                                            style="
                                                                              text-transform: uppercase;
                                                                            "
                                                                            >l</span
                                                                          ><a
                                                                            href="https://www.assetra.xyz/blog"
                                                                            target="_blank"
                                                                            style="
                                                                              text-decoration: none;
                                                                              color: #f9eae7;
                                                                            "
                                                                            ><span
                                                                              >Øg</span
                                                                            ></a
                                                                          ><span
                                                                            >﻿</span
                                                                          >
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
                                            </td>
                                            <td
                                              class="pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td
                                                                class="pc-w620-spacing-0-0-0-0"
                                                                valign="top"
                                                              >
                                                                <table
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  width="100%"
                                                                  style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <td
                                                                      valign="top"
                                                                      class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                      align="center"
                                                                      style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      "
                                                                    >
                                                                      <a
                                                                        class="pc-font-alt pc-w620-textAlign-center pc-w620-fontSize-13px"
                                                                        href="https://www.assetra.xyz/"
                                                                        target="_blank"
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
                                                                        "
                                                                      >
                                                                        <span
                                                                          >Ø</span
                                                                        ><span
                                                                          style="
                                                                            text-transform: uppercase;
                                                                          "
                                                                          >UR
                                                                          ST</span
                                                                        ><span
                                                                          >Ø</span
                                                                        ><span
                                                                          style="
                                                                            text-transform: uppercase;
                                                                          "
                                                                          >RY</span
                                                                        >
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
                                            <td
                                              class="pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 10px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td
                                                                class="pc-w620-spacing-0-0-0-0"
                                                                valign="top"
                                                              >
                                                                <table
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  role="presentation"
                                                                  width="100%"
                                                                  style="
                                                                    border-collapse: separate;
                                                                    border-spacing: 0;
                                                                  "
                                                                >
                                                                  <tr>
                                                                    <td
                                                                      valign="top"
                                                                      class="pc-w620-padding-0-0-0-0 pc-w620-textAlign-center"
                                                                      align="center"
                                                                      style="
                                                                        padding: 0px
                                                                          0px
                                                                          0px
                                                                          0px;
                                                                      "
                                                                    >
                                                                      <div
                                                                        class="pc-font-alt pc-w620-textAlign-center pc-w620-fontSize-13px"
                                                                        style="
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
                                                                        "
                                                                      >
                                                                        <div>
                                                                          <span
                                                                            >&#xFEFF;</span
                                                                          ><a
                                                                            href="mailto:support@assetra.xyz"
                                                                            target="_blank"
                                                                            style="
                                                                              text-decoration: none;
                                                                              color: #f9eae7;
                                                                            "
                                                                            ><span
                                                                              style="
                                                                                text-transform: uppercase;
                                                                              "
                                                                              >SUPP</span
                                                                            ><span
                                                                              >Ø</span
                                                                            ><span
                                                                              style="
                                                                                text-transform: uppercase;
                                                                              "
                                                                              >RT</span
                                                                            ></a
                                                                          ><span
                                                                            >&#xFEFF;</span
                                                                          >
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
                                            </td>
                                            <td
                                              class="pc-grid-td-last pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 10px;
                                              "
                                            >
                                              <table
                                                class="pc-w620-width-hug"
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    class="pc-w620-padding-0-0-0-0"
                                                    align="center"
                                                    valign="middle"
                                                    style="
                                                      padding: 0px 0px 0px 0px;
                                                    "
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                            align="center"
                                                            style="
                                                              border-collapse: separate;
                                                              border-spacing: 0;
                                                            "
                                                          >
                                                            <tr>
                                                              <td
                                                                valign="top"
                                                                align="center"
                                                              >
                                                                <a
                                                                  class="pc-font-alt pc-w620-fontSize-13px"
                                                                  href="https://www.assetra.xyz/"
                                                                  target="_blank"
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
                                                                  "
                                                                >
                                                                  <span
                                                                    style="
                                                                      text-transform: uppercase;
                                                                    "
                                                                    >FAQ</span
                                                                  >
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
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                    style="width: 100%"
                                  >
                                    <tr>
                                      <td
                                        valign="top"
                                        style="padding: 0px 0px 32px 0px"
                                      >
                                        <table
                                          class="pc-w620-width-270"
                                          width="300"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          style="margin: auto"
                                        >
                                          <tr>
                                            <!--[if gte mso 9]>
                                              <td
                                                height="1"
                                                valign="top"
                                                style="
                                                  line-height: 1px;
                                                  font-size: 1px;
                                                  border-bottom: 1px solid
                                                    #a9776c;
                                                "
                                              >
                                                &nbsp;
                                              </td>
                                            <![endif]-->
                                            <!--[if !gte mso 9]><!-- -->
                                            <td
                                              height="1"
                                              valign="top"
                                              style="
                                                line-height: 1px;
                                                font-size: 1px;
                                                border-bottom: 1px solid #a9776c;
                                              "
                                            >
                                              &nbsp;
                                            </td>
                                            <!--<![endif]-->
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        align="center"
                                        style="padding: 0px 0px 28px 0px"
                                      >
                                        <table
                                          class="pc-width-hug pc-w620-gridCollapsed-0"
                                          align="center"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                        >
                                          <tr
                                            class="pc-grid-tr-first pc-grid-tr-last"
                                          >
                                            <td
                                              class="pc-grid-td-first pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 0px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="center"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <a
                                                                  href="https://www.linkedin.com/company/assetradotcom/"
                                                                  target="_blank"
                                                                >
                                                                  <img
                                                                    src="https://cloudfilesdm.com/postcards/b2b95cedb69af95b9209bb375b1e0996.png"
                                                                    class=""
                                                                    width="20"
                                                                    height="20"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      outline: 0;
                                                                      line-height: 100%;
                                                                      -ms-interpolation-mode: bicubic;
                                                                      width: 20px;
                                                                      height: 20px;
                                                                    "
                                                                    alt=""
                                                                  />
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
                                            <td
                                              class="pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="center"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <a
                                                                  href="https://x.com/assetradotxyz"
                                                                  target="_blank"
                                                                >
                                                                  <img
                                                                    src="https://cloudfilesdm.com/postcards/feea36d23d731ae10d42f7f5ef39f688.png"
                                                                    class=""
                                                                    width="20"
                                                                    height="20"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      outline: 0;
                                                                      line-height: 100%;
                                                                      -ms-interpolation-mode: bicubic;
                                                                      width: 20px;
                                                                      height: 20px;
                                                                    "
                                                                    alt=""
                                                                  />
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
                                            <td
                                              class="pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="center"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <a
                                                                  href="https://www.instagram.com/assetradotxyz"
                                                                  target="_blank"
                                                                >
                                                                  <img
                                                                    src="https://cloudfilesdm.com/postcards/b01bc93061ef80b1e939305054c5ad54.png"
                                                                    class=""
                                                                    width="20"
                                                                    height="20"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      outline: 0;
                                                                      line-height: 100%;
                                                                      -ms-interpolation-mode: bicubic;
                                                                      width: 20px;
                                                                      height: 20px;
                                                                    "
                                                                    alt=""
                                                                  />
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
                                            <td
                                              class="pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 16px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="center"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <a
                                                                  href="https://discord.com/invite/dVmMCdf9jx"
                                                                  target="_blank"
                                                                >
                                                                  <img
                                                                    src="https://cloudfilesdm.com/postcards/c46d8be385fea4f427e2502a6a224747.png"
                                                                    class=""
                                                                    width="20"
                                                                    height="20"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      outline: 0;
                                                                      line-height: 100%;
                                                                      -ms-interpolation-mode: bicubic;
                                                                      width: 20px;
                                                                      height: 20px;
                                                                    "
                                                                    alt=""
                                                                  />
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
                                            <td
                                              class="pc-grid-td-last pc-w620-itemsSpacings-20-0"
                                              valign="middle"
                                              style="
                                                padding-top: 0px;
                                                padding-right: 0px;
                                                padding-bottom: 0px;
                                                padding-left: 16px;
                                              "
                                            >
                                              <table
                                                style="
                                                  border-collapse: separate;
                                                  border-spacing: 0;
                                                "
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                              >
                                                <tr>
                                                  <td
                                                    align="center"
                                                    valign="middle"
                                                  >
                                                    <table
                                                      align="center"
                                                      width="100%"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      role="presentation"
                                                      style="width: 100%"
                                                    >
                                                      <tr>
                                                        <td
                                                          align="center"
                                                          valign="top"
                                                        >
                                                          <table
                                                            align="center"
                                                            border="0"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            role="presentation"
                                                          >
                                                            <tr>
                                                              <td valign="top">
                                                                <a
                                                                  href="https://www.facebook.com/profile.php?id=61565050207514&mibextid=ZbWKwL"
                                                                  target="_blank"
                                                                >
                                                                  <img
                                                                    src="https://cloudfilesdm.com/postcards/37e4df77707133bd850fcf701e04e2ce.png"
                                                                    class=""
                                                                    width="20"
                                                                    height="20"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      outline: 0;
                                                                      line-height: 100%;
                                                                      -ms-interpolation-mode: bicubic;
                                                                      width: 20px;
                                                                      height: 20px;
                                                                    "
                                                                    alt=""
                                                                  />
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
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        align="center"
                                        valign="top"
                                        style="padding: 0px 20px 32px 20px"
                                      >
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          width="100%"
                                          style="
                                            border-collapse: separate;
                                            border-spacing: 0;
                                            margin-right: auto;
                                            margin-left: auto;
                                          "
                                        >
                                          <tr>
                                            <td valign="top" align="center">
                                              <div
                                                class="pc-font-alt"
                                                style="
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
                                                "
                                              >
                                                <div>
                                                  <span
                                                    >Need assistance or have
                                                    questions</span
                                                  ><span
                                                    style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    "
                                                    >? </span
                                                  ><span>Click </span
                                                  ><a
                                                    href="mailto:support@assetra.xyz"
                                                    target="_blank"
                                                    style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "
                                                    ><span
                                                      style="
                                                        text-decoration: underline;
                                                        font-weight: 400;
                                                        font-style: normal;
                                                      "
                                                      >here</span
                                                    ></a
                                                  ><span
                                                    style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    "
                                                  >
                                                  </span
                                                  ><span
                                                    >to contact our support
                                                    team. </span
                                                  ><span
                                                    style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    "
                                                    >You can view our privacy
                                                    policy </span
                                                  ><a
                                                    href="https://www.assetra.xyz/policy"
                                                    target="_blank"
                                                    style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "
                                                    ><span
                                                      style="
                                                        text-decoration: underline;
                                                        font-weight: 400;
                                                        font-style: normal;
                                                      "
                                                      >here</span
                                                    ></a
                                                  ><span
                                                    style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                    "
                                                    >.</span
                                                  >
                                                </div>
                                              </div>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                  <table
                                    width="100%"
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                  >
                                    <tr>
                                      <td
                                        align="center"
                                        valign="top"
                                        style="padding: 0px 0px 0px 0px"
                                      >
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          width="100%"
                                          style="
                                            border-collapse: separate;
                                            border-spacing: 0;
                                            margin-right: auto;
                                            margin-left: auto;
                                          "
                                        >
                                          <tr>
                                            <td valign="top" align="center">
                                              <div
                                                class="pc-font-alt"
                                                style="
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
                                                "
                                              >
                                                <div>
                                                  <span
                                                    style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                      color: rgba(
                                                        255,
                                                        255,
                                                        255,
                                                        0.6
                                                      );
                                                    "
                                                    >© 2024</span
                                                  ><a
                                                    href="https://www.assetra.xyz/"
                                                    target="_blank"
                                                    style="
                                                      text-decoration: none;
                                                      color: #ffffff99;
                                                    "
                                                    ><span
                                                      style="
                                                        font-weight: normal;
                                                        font-style: normal;
                                                        color: rgba(
                                                          255,
                                                          255,
                                                          255,
                                                          0.6
                                                        );
                                                      "
                                                    >
                                                      Assetra</span
                                                    ></a
                                                  ><span
                                                    style="
                                                      font-weight: 400;
                                                      font-style: normal;
                                                      color: rgba(
                                                        255,
                                                        255,
                                                        255,
                                                        0.6
                                                      );
                                                    "
                                                    >. All Rights
                                                    Reserved.</span
                                                  >
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
    <div
      class="pc-gmail-fix"
      style="white-space: nowrap; font: 15px courier; line-height: 0"
    >
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    </div>
  </body>
</html>
        """


@app.route("/send_email", methods=["POST"])
def send_email():
    data = request.get_json()
    email = data.get("email")
    code = data.get("code")

    if not email or not code:
        return jsonify({"error": "Email and verification link are required"}), 400

    try:
        # Generate the email content
        html_content = generate_email_content(code)

        # Create and send the email
        msg = Message(
            subject="Welcome to Assetra - Your Gateway to Digital Assets!",
            recipients=[email],  # Must be a list
            html=html_content,
        )
        mail.send(msg)
        return jsonify({"message": f"Email sent to {email}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
