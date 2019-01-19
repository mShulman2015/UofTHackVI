/*
This file is responsible for creating the redux store and injecting middleware
*/
import { applyMiddleware, createStore } from 'redux';
import reducer from "./reducers"

// this is a used for easy debugging via browser console, with colorful displays
// to highlight state before and after transition.
import logger from "redux-logger"

// this is used to delay dispatches of events, allowing us to return functions that
// dispatch events to the store once the conditions are satified. This allows us to
// wait for async function to receive data back before dispatching the event with a payload.
// Checkout the example.js file under Actions folder.
import thunk from "redux-thunk"

// this is a easy way to handle promises in reducers by removing the need to writeout
// function calls for transition states.
// Checkout the exampleReducer2.js file under Reducers
import promise from "redux-promise-middleware"

const middleware = applyMiddleware(promise(), thunk, logger)
export default createStore(reducer, middleware)
