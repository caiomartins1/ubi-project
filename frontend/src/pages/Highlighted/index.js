import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';

import highlightedIcon from '../../assets/icons/highlighted-icon.png';

import './index.css';

function Highlighted() {

  const [highlightedEvents, setHighlightedEvents] = useState([]);

  useEffect(() => {
    async function getHighlightedEvents() {
      const response = await api.get('/contenthighlights');
  
      const filteredUpsellingEvents = await Promise.all(response.data.map(
        async(upsellingEvent) => {
          return await getUpsellingEventCardData(upsellingEvent.content);
        }
  
      ));
  
      setHighlightedEvents(filteredUpsellingEvents);
    }

    getHighlightedEvents();
  }, []);

  async function getUpsellingEventCardData(eventId) {
    const response = await api.get(`/contents/${eventId}`);

    const { uuid, title, country, city, image } = response.data;

    return { uuid, title, country, city, image };
  }

  return (
    <ListEvents title="Highlighted" typeIcon={highlightedIcon} eventsArray={highlightedEvents}/>
  );
}

export default Highlighted;