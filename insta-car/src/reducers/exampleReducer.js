/**
* This reducer is used for handling all state changes for a display component
*/

//specifying initial state of the component
const initialState = {
  attribute1: "",
  attribute2: false,
  attribute3: 0
}

const eventReducer = (state = initialState, action) => {
  // action has 2 attribute, type and payload, type determines what is happening
  // payload is the data used to mutate the state.
  switch (action.type) {
    // By convention via online redux documentation, use ALL_CAPS for cases
    case "EXAMPLE":
      //checkout ES6 Spread syntax if you're not sure what {...Object} is doing
      return { ...state, attribute2: true }

    case "ANOTHER_EXAMPLE":
      return { ...state, attribute2: false, attribute3: action.payload }
    default: return state;
  }
}

export default eventReducer
