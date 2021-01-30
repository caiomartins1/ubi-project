// TODO: Validate which events will display (Active field on model)

import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';

import upsellingIcon from '../../assets/icons/upselling-icon.png';

import './index.css';

function Upselling() {

  const [upsellingEvents, setUpsellingEvents] = useState([]);

  useEffect(() => {
    async function getUpsellingEvents() {
      const response = await api.get('/contentupselling');
  
      const filteredUpsellingEvents = await Promise.all(response.data.map(
        async(upsellingEvent) => {
          return await getUpsellingEventCardData(upsellingEvent.content);
        }
  
      ));
  
      setUpsellingEvents(validateUpsellingEvents(filteredUpsellingEvents));
    }

    getUpsellingEvents();
  }, []);

  function validateUpsellingEvents(eventsArray) {
    return eventsArray.filter((event) => event !== 'undefined' && event !== null);
  }

  async function getUpsellingEventCardData(eventId) {
    const response = await api.get(`/contents/${eventId}`);

    const { uuid, title, country, city, image, active } = response.data;

    if (!active) return null;
    
    return { uuid, title, country, city, image };
  }

  return (
    <ListEvents title="Upselling" typeIcon={upsellingIcon} eventsArray={upsellingEvents}/>
  );
}

export default Upselling;