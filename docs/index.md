# bank2ynab

A common project to consolidate all conversion efforts from various banks' export formats into YNAB's import format.

- [What? (Features)](#what)
  - [Wish List](#wishlist)
- [Why?](#why)
- [How?](#how)
- [Installation Instructions](#install)
  - [Requirements](#requirements)
- [User Guide](#userguide)
- [YNAB API Import](#api)
- [Known Bugs](#knownbugs)
- [List of Supported Banks](#formats)

## <a name="what"></a>What? (Features)

***Convert your downloaded bank statements into YNAB's input format.*** Here's what this script does, step by step:

1. Look for and parse the `bank2ynab.conf`. This file contains all the rules and import formats.
1. Look for and parse every CSV file in the configured download directory.
1. If the CSV file matches any of the configured formats:
   1. Create a new CSV file in YNAB's CSV format with the correct columns and a blank Category column.
   1. Optionally delete the original CSV file.

### <a name="wishlist"></a>Wish List

- add many more input formats from all the [other YNAB-CSV-conversion projects](https://github.com/search?o=desc&q=ynab+convert&s=updated&type=Repositories&utf8=%E2%9C%93).
- maybe coming later: automatically download your bank statements? (uses external services; only available in some countries)
- maybe coming later: automatically import the converted data into your YNAB app? (optional, default off)

## <a name="why"></a>Why?

There are currently more than 80 GitHub projects related to YNAB converter scripts. Clearly there's a need, but until now these solutions have been fragmented. The present project "bank2ynab" aims to focus the efforts on a common source that encapsulates a large number of bank formats. This will also provide a common basis for a solution using a variety of programming languages.

## <a name="how"></a>How? Contribute!

- If you're "just a user":
  - [tell us your import format](https://goo.gl/forms/b7SNwTxmQFfnXlMf2) and we can create a converter - for you and for everyone else!
  - use the converter provided here and [give us feedback](https://github.com/bank2ynab/bank2ynab/issues/new/choose) - or participate!
- If you've already built a YNAB converter:
  - take advantage of this project to get more import formats.
  - give back to this project by [sharing your existing import formats](https://goo.gl/forms/b7SNwTxmQFfnXlMf2).
- Add a brainstorming item as a [new issue](https://github.com/bank2ynab/bank2ynab/issues/new).
- Join the chat over at https://gitter.im/bank2ynab/Lobby
- See also: [the wiki](https://github.com/bank2ynab/bank2ynab/wiki), perhaps most importantly [this page about import formats](https://github.com/bank2ynab/bank2ynab/wiki/ImportFormats).

## <a name="install"></a>Installation Instructions

- Install from PyPI: `pip install bank2ynab`
- Or install from source:
  - `git clone https://github.com/bank2ynab/bank2ynab.git`
  - `cd bank2ynab`
  - `uv sync`
- Then follow the [User Guide](#userguide) below.

### <a name="requirements"></a>Requirements

- Windows or Mac or Linux
- Python v3.9+ installed ([download it from python.org](https://www.python.org/downloads/))
- Support for other scripting languages may follow. Contributions are welcome!

Troubleshooting:
- If you see `RequestsDependencyWarning` about `urllib3/chardet/charset_normalizer`, resync the environment with `uv sync --reinstall`.

## <a name="userguide"></a>User Guide

Using `bank2ynab` is easy:

1. Download some bank statements from your banking website.
   - Make sure to choose CSV format. Save with the default suggested filename so that the converter can find it.
   - It's okay if the statements contain data that you already have in YNAB. YNAB will detect and skip these.
1. Run `bank2ynab` once to generate default config files in your user config directory (`BANK2YNAB_CONFIG_DIR` if set, otherwise the OS default for `bank2ynab`).
1. Check the `[DEFAULT]` configuration in `user_configuration.conf`.
   - `Source Path = c:\users\example-username\Downloads`
   - `Delete Source File = True` or `False`
1. Check that `bank2ynab.conf` contains a `[SECTION]` for your bank format.
1. Run the converter:
   - If installed from PyPI: `bank2ynab`
   - If running from source: `uv run bank2ynab`
1. If API upload is not configured, import the output CSV manually in YNAB.

## <a name="api"></a>YNAB API Import

1. Create a Personal Access Token in YNAB (`My Account` -> `Developer Settings` -> `Personal Access Tokens`).
1. Open `user_configuration.conf` and set `YNAB API Access Token = <your_token>`.
1. Run `bank2ynab`.
1. On first API run for each bank section, choose budget and account.
1. The mapping is saved as `YNAB Account ID = <budget_id>||<account_id>`.

Notes:
- Config location:
  - `BANK2YNAB_CONFIG_DIR` if set.
  - Otherwise your OS default user config directory for `bank2ynab`.
- Root-level config files in the project directory are no longer used.
- If `Save YNAB Account = True`, mapping is reused automatically.
- If token is blank, API upload is skipped and output remains CSV-based.

## <a name="knownbugs"></a>Known Bugs

For details, please see our [issue list labeled "Bug"](https://github.com/bank2ynab/bank2ynab/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

## <a name="formats"></a>List of Supported Banks

Here is a list of the banks and their formats that we already support. Note that we have many [more formats in the pipeline](https://github.com/bank2ynab/bank2ynab/issues?q=is%3Aopen+is%3Aissue+label%3A%22bank+format%22) so the list continues to grow, and we are happy to receive [requests](https://goo.gl/forms/b7SNwTxmQFfnXlMf2). In alphabetical order (country and bank):

1. AT easybank credit card
1. AT Raiffeisen Bank 2018 checking
1. AT Raiffeisen Bank 2019 checking
1. AT Raiffeisen Bank VISA card
1. BE KBC checking
1. BE BE Keytrade Bank
1. BR Banco do Brasil checking
1. BR Inter checking
1. CA TD Canada Trust, checking+Visa
1. CH Zürcher Kantonalbank, Kontoauszug
1. , Finanzassistent
1. CZ AirBank checking and savings
1. CZ Ceska Sporitelna
1. CZ Raiffeisen bank
1. DE Commerzbank checking
1. DE Consorsbank checking
1. DE Deutsche Bank
1. DE Deutsche Kreditbank checking
1. DE Deutsche Kreditbank credit card
1. DE ING-DiBa
1. DE Kreissparkasse
1. DE N26
1. DE Ostseesparkasse Rostock checking
1. DE Ostseesparkasse Rostock credit card
1. DE Sparkasse Rhein-Neckar-Nord
1. DK Bankernes EDB Central
1. DK Jyske Bank VISA
1. DK Nordea
1. DK Sparkassen Thy
1. HU Erste Bank checking
1. IE AIB Ireland
1. IE Bank of Ireland
1. IE N26
1. IE Ulster Bank, savings
1. MV Bank of Maldives, checking
1. NL Bunq checking
1. NL bunqDesktop software
1. NL ING Bank
1. NL Rabobank (2017 format)
1. NL Rabobank (2018 format)
1. NO DNB
1. NO Sparebank 1 VISA
1. PL mBank, checking
1. SE Handelsbanken
1. SE Länsförsäkringar checking
1. SE Nordea
1. SE SEB, Skandinaviska Enskilda Banken
1. SE Sparbanken Tanum
1. SE Swedbank
1. SE Swedbank (2019 format)
1. SE OCBC Bank
1. SG POSB savings
1. SK Tatra Banka
1. SK VUB
1. UK Barclaycard credit card
1. UK Barclaycard Business Credit Card
1. UK Co-operative Bank
1. UK first direct checking
1. UK Monzo checking
1. US Bank of America
1. US Bank of America Credit Card
1. US BB&T
1. US Chase Credit Card
1. US Schwab
1. US TB Bank
1. (software) Mint
1. (software) Neteller
1. (software) Personal Capital

----

[![XKCD on standards: Fortunately, the charging one has been solved now that we've all standardized on mini-USB. Or is it micro-USB? Shit.](https://imgs.xkcd.com/comics/standards.png)](https://xkcd.com/927/)

----

*Disclaimer: Please use at your own risk. This tool is neither officially supported by YNAB (the company) nor by YNAB (the software) in any way. Use of this tool could introduce problems into your budget that YNAB, through its official support channels, will not be able to troubleshoot or fix. See also the full [MIT licence](https://raw.githubusercontent.com/bank2ynab/bank2ynab/master/LICENSE).*

