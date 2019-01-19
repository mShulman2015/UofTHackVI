/*
This file is used to render the entire application onto the webpage
*/
import React from 'react';
import ReactDOM from 'react-dom';
import Root from './components/root';
import store from './store'

ReactDOM.render(<Root store={store}/>, document.getElementById('root'));
