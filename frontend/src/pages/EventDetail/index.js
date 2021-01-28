import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import L from 'leaflet';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { Carousel } from 'react-bootstrap';
import TopNav from '../../components/TopNav';

import locationIcon from '../../assets/icons/location-icon.png';
import exploreIcon from '../../assets/icons/explore-icon.png';
import directionsIcon from '../../assets/icons/directions-icon.png';

import 'leaflet/dist/leaflet.css';
import './index.css';

function EventDetail(props) {

  const [eventDetailed, setEventDetailed] = useState({});

  const locationIconLeaflet = L.icon({
    iconUrl: locationIcon,
  });

  useEffect(() => {
    const { eventId } = props.location.state; 

    async function getEventDetails(id) {
      const response = await api.get(`/contents/${id}`);
      const filteredEvent = filterEventDetailsToEventObject(response.data);
      setEventDetailed(filteredEvent);
    }

    getEventDetails(eventId);
  });

  function filterEventDetailsToEventObject(responseData) {
    const { title, city, description, latitude, longitude, image, image_02, image_03 } = responseData;
    const images = [image, image_02, image_03];

    const event =  {
      title,
      city,
      description,
      latitude,
      longitude,
      images
    }

    return event;
  }

  function handleDirectionsClick() {
    window.location = `https://www.google.com/maps/@${eventDetailed.latitude},${eventDetailed.longitude},15z`;
  }

  return (
    <div className="event-detail-page">
      <TopNav title={'Attraction'} typeIcon={exploreIcon}/>

      <div className="event-detail-scroll">
        <div className="event-detail-info">
          <h1 className="event-detail-name">{`${eventDetailed.title}, `}{eventDetailed.city}</h1>

          <h3 className="event-detail-description">{eventDetailed.description}</h3>
        </div>

        <div className="event-detail-location">
          <div className="event-detail-map">
          {eventDetailed.latitude && eventDetailed.longitude && 
            <MapContainer 
              center={[eventDetailed.latitude, eventDetailed.longitude]} 
              zoom="4" 
              scrollWheelZoom={false}
              style={{height: "400px", width: "100%"}}
            >
              <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />

              <Marker position={[eventDetailed.latitude, eventDetailed.longitude]} icon={locationIconLeaflet}>
                <Popup>
                  {eventDetailed.title}
                </Popup>
              </Marker>
            </MapContainer>
          }
          </div>
          <div className="event-detail-directions-buttom" onClick={handleDirectionsClick}>
            <img src={directionsIcon} alt="" className="event-detail-directions-buttom-icon"/>
            <p className="event-detail-directions-buttom-title">Directions</p>
          </div>
        </div>

        <div className="event-detail-gallery">
          <h1 className="event-detail-gallery-title">Gallery</h1>
          <div className="event-detail-gallery-carousel">
            <Carousel>

              {
                eventDetailed.images ? 
                eventDetailed.images.map(image => {
                  return (
                    <Carousel.Item key={image}>
                      <img
                        className="d-block w-100 event-detail-gallery-image"
                        src={image}
                        alt="First slide"
                      />
                    </Carousel.Item>
                  )
                })
                : <></>

              }
            </Carousel>
          </div>
        </div>
      </div>
      
    </div>
  )
}

// https://www.google.com/maps/place/Addu+City,+Maldives/@-0.6415704,73.1542683,12z/data=!3m1!4b1!4m5!3m4!1s0x24b59ec91fa7961b:0xaf04ff732e934ada!8m2!3d-0.6300995!4d73.1585626

export default EventDetail;
