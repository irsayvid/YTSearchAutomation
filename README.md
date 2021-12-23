# YouTube Search Automation

---

An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response

## Requirements

- [Python](https://www.python.org/downloads/) latest version preferred
- [Google account](https://accounts.google.com/SignUp?hl=nn)
- [Python Package Index](https://pip.pypa.io/en/stable/installation/)

## Steps to run this Project locally

- Clone the repo using

  ```
  git clone https://github.com/irsayvid/YTSearchAutomation.git
  ```

- Learn how to [generate API key](./DOCUMENTATION.md#GenerateYouTubedataAPIkey) and store the API key(s) in apikeys.json

- Now set up local environment and install the requirements in your virtual environment. You can get the instructions [here](./DOCUMENTATION.md).

- Run the app using the following command
  ```
  python manage.py runserver
  ```

### URLs and their responses

- _/_ : makes request to the API and stores 15 results in the DB. Default query is chess. Can be changed by changing input in search bar.

- _/fetchresults_ : Dislays all responses stores in DB in tabular form paginated. Each page is limited to 8 responses.

- _/fetchresults/2/_ : Displays responses present in page 2 (2 can be replaced by any number). If number exceeds max pages available, it diplays last page available.

- _/fetchresults/chess/_ : Displays responses filtering title and search query for word chess. It displays if there's a partial match in either of them.

- _/fetchresults/chess/3/_ : Displays responses present in page 3 filtering title and search query for word chess. It displays if there's a partial match in either of them.
