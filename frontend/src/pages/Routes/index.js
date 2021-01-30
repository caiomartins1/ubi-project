import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';

import routesIcon from '../../assets/icons/routes-icon.png';

import './index.css';

function Routes() {
  
  const [events, setEvents] = useState([]);

  useEffect(() => {
    async function createRoutes() {
      const routeParents = await getRoutesParents();
      setEvents(createCustomEventWithRouteParents(routeParents));
    }

    async function getRoutesParents() {
      const response = await api.get('/contents');

      const possibleRoutes = response.data.filter((event) => event.active && event.is_parent);

      const eventsWithSiblings = await Promise.all(possibleRoutes.map(async(event) => {
        const siblings =  await countSiblings(event.uuid);

        if (siblings < 1) return null;

        return event;
      }));

      return eventsWithSiblings.filter(event => event !== null)

    }
    createRoutes();
  }, []);


  async function countSiblings(parentId) {
    const response = await api.get('/contentsiblings');

    let siblings = 0;
    
    for (const item of response.data) {
      if (item.parent === parentId) {
        siblings++;
      }
    }

    return siblings;
  }

  function createCustomEventWithRouteParents(parentsArray) {
      const customEvents = parentsArray
        .map((event, index) => {
          return {
            image: event.image,
            title: `Route #${index + 1}`,
            city: event.country,
            id: event.uuid
          }
        });
  
      return customEvents;
  }


  return (
    <ListEvents title="Routes" typeIcon={routesIcon} eventsArray={events} isRoute={true}/>
  );
}

export default Routes;
