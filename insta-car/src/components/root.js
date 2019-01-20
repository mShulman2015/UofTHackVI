/*
This file is intended for grouping all the component into the application,
and provide routing for the application
*/
import React from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Provider } from 'react-redux'
import PropTypes from 'prop-types';

import FindCar from './findCar/findCar';
import InstaCarNavbar from './instacarNavbar/instacarNavbar';
import MyCar from './myCar/myCar'
//import CarRegistration from './carRegistration/carRegistration'

// Just add your component onto a path below
const Root = ({ store }) => (
  <Provider store={store}>
    <Router>

        <div>
        <InstaCarNavbar/>
        <Route exact path="/" component={FindCar} />
        <Route exact path="/cars/:car_id" component={MyCar}/>
        </div>
    </Router>
  </Provider>
)

Root.propTypes = {
  store: PropTypes.object.isRequired
}

export default Root;
