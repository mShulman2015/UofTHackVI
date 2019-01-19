/*
This file exports functions that dispatch events to the store.
*/


/*
* This is a set of action called directly within a component, the example action
* first dispatches the type, which is handled within the switch statment within the reducers
* then the payload, with is the data used to mutate the current state.
*/

// Normally without the redux-thunk middleware, would dispatch the event as the
// following:
export const ADD_TODO = 'ADD_TODO'
export function addTodo(text) {
    // here we specify the type and payload in an object and returning it right away
    return { type: ADD_TODO, text }
}

// However with redux-thunk middleware, we can now delay the dispatch by returning
// a function instead. The dispatch function will be passed in via the parameter in the component.


// we can create a function that takes a parameter and attach it as a payload
// to update some attribute to the store
export function newProjectSubmit() {
    return function (dispatch) {
        dispatch({
            type: "FETCH_EVENT2_FULFILLED",

        })

    }
}

//an async function that return a promise that will eventually resolve by returning v
function delay(t,v) {
    return new Promise(function(resolve) {
        setTimeout(resolve.bind(null, v), t)
    });
}
