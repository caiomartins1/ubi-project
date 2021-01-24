

import React from 'react';

import rightArrowIcon from '../../assets/icons/right-arrow-icon.png';
import locationIcon from '../../assets/icons/location-icon.png';
import sampleImage from '../../assets/sample-card-img.png';

import './index.css';

function EventCard() {
  return (
    <div className="list-events-card">
      <img src={sampleImage} alt="" className="list-events-card-image"/>

      <div className="list-events-card-info">
        <p className="list-events-card-title">Helicopter Adventure,</p>

        <div className="list-events-card-location-container">
          <img src={locationIcon} alt="" className="list-events-card-location-icon"/>

          <p className="list-events-card-city">Addu City</p>

          <img src={rightArrowIcon} alt="" className="list-events-card-right-arrow"/>
        </div>
      </div>
    </div>
  );
}

export default EventCard;
