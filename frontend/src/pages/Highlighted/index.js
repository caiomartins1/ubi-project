import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';
import langs from '../../lang/lang';


import highlightedIcon from '../../assets/icons/highlighted-icon.png';

import './index.css';

function Highlighted() {

  const [highlightedEvents, setHighlightedEvents] = useState([]);

  const [lang, ] = useState(
    localStorage.getItem('lang') || 'en'
  );

  useEffect(() => {
    async function getHighlightedEvents() {
      const response = await api.get('/contenthighlights');
  
      const filteredHighlightedEvents = await Promise.all(response.data.map(
        async(highlightedEvent) => {

          if (isActiveHighlight(highlightedEvent)) {
            return await getHighlightEventCardData(highlightedEvent.content);
          }
        }
  
      ));
        
      setHighlightedEvents(validateHighlightedEvents(filteredHighlightedEvents));
    }

    getHighlightedEvents();
  }, []);

  function isActiveHighlight(highlight) {
    const startDate = new Date(highlight.start_date);
    const endDate = new Date(highlight.end_date);
    const nowDate = new Date(Date.now());

    if (highlight.is_always) return true;

    return ((nowDate >= startDate) && (nowDate < endDate));
  }

  function validateHighlightedEvents(eventsArray) {
    return eventsArray.filter((event) => typeof event !== 'undefined' && event !== null);
  }

  async function getHighlightEventCardData(eventId) {
    const response = await api.get(`/contents/${eventId}`);

    const { uuid, title, country, city, image, active } = response.data;

    if (!active) { return null };

    return { uuid, title, country, city, image };
  }

  return (
    <ListEvents title={langs['home'][lang].highlighted} typeIcon={highlightedIcon} eventsArray={highlightedEvents}/>
  );
}

export default Highlighted;