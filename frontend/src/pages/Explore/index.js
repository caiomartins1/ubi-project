import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';
import langs from '../../lang/lang';

import exploreIcon from '../../assets/icons/explore-icon.png';

import './index.css';

function Explore() {

  const [events, setEvents] = useState([]);
  
  const [lang, ] = useState(
    localStorage.getItem('lang') || 'en'
  );
  
  useEffect(() => {

    async function getEvents() {
      const response = await api.get('/contents');
      
      const filteredEvents = response.data
      .filter(event => event.active)
      .map(event => {
        const { uuid, title, city, image } = event;
        return { uuid, title, city, image }
      })
      
      setEvents(filteredEvents);
    }

    getEvents();
  }, [lang]);

  return (
    <ListEvents title={langs['home'][lang].explore} typeIcon={exploreIcon} eventsArray={events}/>
  );
}

export default Explore;
