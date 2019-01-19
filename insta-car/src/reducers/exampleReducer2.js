/**
* This reducer is used for handling all state changes for the specific display
* within a modal component
*/

//specifying initial state of the component
const initialState = {
  content: "",
  fetching: false,
  fetched: true,
  error: null,
  attribute1: false
}

const eventReducer = (state = initialState, action) => {
  switch (action.type) {
    // with the redux promise middleware, for any async handling, all we have to do
    // is add _PENDING, _REJECTED and _FULFILLED to the end of an async event.
    // In the example below, the actual event being dispatched is "FETCH_EVENT"
    // in which the middleware will automatically append _PENDING to it once
    // it detects that "FETCH_EVENT" is a call with a promise. (See in exampleActions.js under actions folder)
    // Lastly, add handling for when the promise is rejected or fullfilled
    case "FETCH_EVENT_PENDING":
      return { ...state, fetching: true }
    case "FETCH_EVENT_REJECTED":
      return { ...state, fetching: false, error: action.payload }
    case "FETCH_EVENT_FULFILLED":
      return {
        ...state,
        fetching: false,
        fetched: true,
        attribute1: action.payload,
      }
    default: return state;
  }
}

export default eventReducer
