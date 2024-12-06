# Software Requirements
The purpose of this document is to list functional and non-functional requirements for the BalanceBuddy financial budgeting application. BalanceBuddy is a budgeting app written in Python to make tracking finances more engaging for users. BalanceBuddy includes the ability to track and log income and expenses while rewarding the user with EXP, representing their dedication to their finances.

|  1  | User Profile    |
|  :-------------------------: | :------------------------------:|
|  FR1  | Users shall be able to sign in to the existing profile |
|  FR2  | Users shall be able to create a new profile |
|  FR3  | User profile shall be able to update user name, password, and email |
|  FR4  | User profiles shall store data related to the user locally |
|  FR5  | User profile shall communicate and update information in the database |

|  2  | Budget tracker    |
|  :-------------------------: | :------------------------------:|
|  FR1  | Users shall be able to log their income|
|  FR2  | Income tracker shall contain log date, name of income source, and an amount|
|  FR3  | Income tacker shall calculate total income in the past week|
|  FR4  | Users shall be able to log their expenses|
|  FR5  | Expense tracker shall contain log date, name of expense source, and an amount|
|  FR6  | Expense tacker shall calculate total expenditure in the past week|

|  3  | GUI    |  
|  :-------------------------: | :------------------------------:|
|  FR1  | The application shall use an intuitive easy to navigate UI |
|  FR2  | The application shall use a unified color palette for all sections |
|  FR3  | GUI shall have a dedicated page for each function |
|  FR4  | GUI shall pull information from the database on login |
|  FR5  | Page tabs shall be accessible from all pages in the app |

# Non-Functional Requirements
|  1  | UI    |
|  :-------------------------: | :------------------------------:|
|  NFR1  | Admins shall be able to post new events for all users|
|  NFR2  | Users Shall be able to receive notifications to log their daily income/expenses|
|  NFR3  | Income tracker shall display recent or total income on a graph|
|  NFR4  | Expense tracker shall display recent or total expenses on a graph|
|  NFR5  | GUI shall have a quick access tab for user settings |

|  2  | Online functions    |
|  :-------------------------: | :------------------------------:|
|  NFR1  | A leaderboard shall display global or friend rankings|
|  NFR2  | The leaderboard shall only display non-sensitive information such as level, EXP, or consecutive days using the app|
|  NFR3  | Users shall be able to send and receive friend requests |
|  NFR4  | Users shall receive EXP for logging expenses and income |
|  NFR5  | Gaining more EXP shall increase users' level |

|  3  | Functionality    |
|  :-------------------------: | :------------------------------:|
|  NFR1  | BalanceBuddy shall run on MacOS and Windows 11|
|  NFR2  | BalanceBuddy shall remember the logged-in user on startup|
|  NFR3  | BalanceBuddy shall have a quick-access menu that contains a link to all pages in the application|
|  NFR4  | Password shall be hidden during log-in|
|  NFR5  | Data stored in the database shall be encrypted|

# Software Artifacts
This section contains links to key documents used in the development of the  BalanceBuddy application.

[Use Case Diagram](https://github.com/JamesZesiger/gvsu-cis350-Software-Innovators/blob/main/artifacts/Use_Case_Diagram.png)

[Gantt Chart](https://github.com/JamesZesiger/gvsu-cis350-Software-Innovators/blob/main/artifacts/Software%20Innovators%20_%20Balance%20Buddy%20_%20Gantt%20Chart%20-%20Detailed%20Version%20V1.0%20(1).pdf)

[Jira](https://software-innovators.atlassian.net/jira/software/projects/SCRUM/boards/1)

[Class Diagram](https://github.com/JamesZesiger/gvsu-cis350-Software-Innovators/blob/main/artifacts/Class%20Diagram.pdf)

[Communications Diagram](https://github.com/JamesZesiger/gvsu-cis350-Software-Innovators/blob/main/artifacts/Communication%20Diagram.pdf)
