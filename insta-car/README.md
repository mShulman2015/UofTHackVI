## Initialize setup
```
npm install
```
## Running Dev Server
In development mode, code is compiled and run on localhost port 3000.
```
npm start
```

## Project Folder Structure
Each new component will have it's own folder under `/components`, with a corresponding reducer under `/reducers` and action under `/actions`. Each reducer and action could have one of two purpose:
- Handle state specific to a component (Most common)
- Handle state specific to a function (This will be for cross component functionalities)

The following is an example of what the project folder will look like
```
react
|
| ->src
|   |
|   |->actions
|   |     |
|   |     |->componentNameAction.js
|   |     |->actionNameAction.js
|   |     ...
|   |
|   |->components
|   |      |
|   |      |-> componentName
|   |      ...      |
|   |               |-> componentName.js
|   |               |-> componentName.css
|   |               
|   |->reducers
|   |      |
|   |      |-> componentNameReducer
|   |      |-> actionNameReducer
```
