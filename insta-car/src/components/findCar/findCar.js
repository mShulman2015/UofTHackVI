import React from 'react'
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import "./findCar.css"
import { Map, InfoWindow, Marker, GoogleApiWrapper } from 'google-maps-react';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import MailIcon from '@material-ui/icons/Mail';
import NavigationIcon from '@material-ui/icons/Navigation';
import Fab from '@material-ui/core/Fab';


//import CarRegistration from "../carRegistration/carRegistration";
var person = require('../assets/person.png');

const drawerStyle = {
    marginLeft: '50px',
    marginRight: '50px'
};

const inputStyle = {
    marginLeft: '20px',
    marginRight: '20px'
};

const btnStyle = {
    width: '50%',
    marginLeft: 'auto',
    marginRight: 'auto'
};

class FindCar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            vehicles: [],
            positions: [],
            vehicle_info: [],
            showingInfoWindow: false,
            activeMarker: {},
            selectedPlace: {},
            markerInfo: "",
            right: false,
            email:"",
            paid: false, 
            referenceNumber: ""
        }
    }

    toggleDrawer = (side, open) => () => {
        console.log("shit fuck");
        this.setState({
            [side]: open,
        }, console.log(this.state.right));
    };

    render() {
        const sideList = (
            <div>
                <List>
                    {[this.state.markerInfo].map((text, index) => (
                        <ListItem key={text}>
                            <ListItemText primary={text} />
                        </ListItem>
                    ))}
                </List>
                <Divider />
            </div>
        );
        return (
            <div>
                <Drawer anchor="right" open={this.state.right} onClose={this.toggleDrawer('right', false)}>
                    <div
                        tabIndex={0}
                        role="button"
                        onClick={this.toggleDrawer('right', false)}
                        onKeyDown={this.toggleDrawer('right', false)}
                        style={drawerStyle}>
                        {sideList}
                    </div>
                    

                    {this.paidButton()}
                </Drawer>
                <Map google={this.props.google} zoom={16}
                    initialCenter={{ lat: 43.659466, lng: -79.396923 }}>

                    <Marker onClick={this.onMarkerClick} name={'Current location'}
                        position={{ lat: 43.659466, lng: -79.396923 }}
                        icon={{
                            url: person,
                            anchor: new this.props.google.maps.Point(32, 32),
                            scaledSize: new this.props.google.maps.Size(50, 50)
                        }} />

                    {this.displayVehicles()}

                    <InfoWindow
                        marker={this.state.activeMarker}
                        visible={this.state.showingInfoWindow}>
                        <div>
                            <h1>{this.state.selectedPlace.name}</h1>
                        </div>
                    </InfoWindow>

                </Map>
            </div>
        )
    }

    displayVehicles() {
        console.log(
            "holy fuck"
        );
        console.log(this.state.positions);
        return (
            <Marker name={this.state.markerInfo} position={this.state.positions[0]} onClick={this.onMarkerClick} />
        )
    }

    paidButton(){
        if (this.state.paid){
            return(
                <Button variant="contained" color="primary" onClick={this.checkIfPaymentComplete}>
                    I Paid!
                </Button>
            )
        }else{
            return(
                <div>
                     <TextField
                        id="outlined-email-input"
                        label="Email ..."
                        type="email"
                        name="email"
                        autoComplete="email"
                        margin="normal"
                        variant="outlined"
                        style={inputStyle}
                        value={this.state.email}
                        onChange={(event)=>{this.setState({email:event.target.value})}}
                    />
                    <Fab variant="extended" color="primary" aria-label="Add" style={btnStyle} onClick={this.sendPaymentRequest}><NavigationIcon />
                        Request 
                    </Fab>
                </div>
            )
        }
    }

    generateInfo() {
        console.log(this.state.vehicle_info[0]);
        let name = ""
        //console.log(this.state.vehicle_info[0][1]);
        if (this.state.vehicle_info[0] !== undefined) {
            name = this.state.vehicle_info[0][1].year + " " + this.state.vehicle_info[0][1].make + " " + this.state.vehicle_info[0][1].model
        }
        this.setState({ markerInfo: name })
        //console.log(name)

    }

    componentDidMount() {
        this.getData()
        console.log(person);
    }

    sortData() {
        var position_curr = new Object();
        var positions = []
        this.state.vehicles.map(element => {
            console.log(element[1].data);
            position_curr = { lat: element[1].data.latitude, lng: element[1].data.longitude }
            positions.push(position_curr)
        })
        this.setState({ positions: positions }, this.displayVehicles)
    }

    async getData() {
        let url = "https://www.mdshulman.com/smartcar/location"
        fetch(url).then(res => res.json()).then(res => {
            this.setState({ vehicles: res }, this.sortData)
        })

        let url2 = "https://www.mdshulman.com/smartcar/vehicle"
        fetch(url2).then(res => res.json()).then(res => {
            this.setState({ vehicle_info: res }, this.generateInfo)
        })
    }

    sendPaymentRequest = ()=> {
        this.setState({paid:true})
        let url = "https://www.mdshulman.com/interac/request-money?amount=68.2&email=" + this.state.email;
        console.log(url)
        fetch(url).then(res => res.json()).then(res => {
            if (res) {
                console.log(res);
                var ref_num = res["request_link"].split("/").pop();
                console.log(ref_num)
                this.setState({referenceNumber: ref_num});
            }
        })
    }

    checkIfPaymentComplete = ()=> {
        let url = "https://www.mdshulman.com/interac/payment-complete?reference_num=" + this.state.referenceNumber;
        console.log(url)
        console.log("Checking")
        fetch(url).then(res => res.json()).then(res => {
            console.log(res);
        })
    }

    onMarkerClick = (props, marker, e) => {
        //this.toggleDrawer('right', true)
        this.setState({
            right: true,
            selectedPlace: props,
            activeMarker: marker,
            showingInfoWindow: true
        });
        //console.log("shit")

    }
}

export default GoogleApiWrapper({
    apiKey: ("AIzaSyDw7rz7Y3P2TO0vSWlJ1tGdlSgDtiV_ryE")
})(FindCar)
