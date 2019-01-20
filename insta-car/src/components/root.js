/*
This file is intended for grouping all the component into the application,
and provide routing for the application
*/
import React from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Provider } from 'react-redux'
import PropTypes from 'prop-types';

import FindCar from './findCar/findCar';
import CarRegistration from './carRegistration/carRegistration'

// Just add your component onto a path below
const Root = ({ store }) => (
  <Provider store={store}>
    <Router>

        <div>
        <CarRegistration/>
        <Route exact path="/" component={FindCar} />
        </div>
    </Router>
  </Provider>
)

Root.propTypes = {
  store: PropTypes.object.isRequired
}

export default Root;
