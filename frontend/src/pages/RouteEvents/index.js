import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';

import routesIcon from '../../assets/icons/routes-icon.png';

import './index.css';

function RouteEvents(props) {

  const [events, setEvents] = useState([]);

  useEffect(() => {
    const { parentId } = props.location.state; 

    async function getRouteEvents(parentId) {
      const response = await api.get('/contentsiblings');
  
      const eventsFilteredByRoute = response.data
        .filter(event => event.parent === parentId);
  
      const eventsCardData = await Promise.all(eventsFilteredByRoute.map(event => {
        return getEventCardData(event.content);
      }));
  
      const parentCardData = await getEventCardData(parentId);
  
      eventsCardData.push(parentCardData);
  
      if (eventsCardData.length > 1) setEvents(filterActiveEvents(eventsCardData));
    }

    getRouteEvents(parentId);
  }, [props.location.state]);

  async function getEventCardData(eventId) {
    const response = await api.get(`/contents/${eventId}`);

    const { uuid, title, country, city, image, active } = response.data;

    if (!active) { return null };

    return { uuid, title, country, city, image };
  }

  function filterActiveEvents(eventCardDataArray) {
    return eventCardDataArray.filter(event => event !== 'undefined' && event !== null);
  }

  return (
    <ListEvents title="Route's Events" typeIcon={routesIcon} eventsArray={events}/>
  );
}

export default RouteEvents;
