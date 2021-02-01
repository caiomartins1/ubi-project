import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import ListEvents from '../../components/ListEvents';

import routesIcon from '../../assets/icons/routes-icon.png';

import './index.css';
import langs from '../../lang/lang';

function Routes() {
  
  const [events, setEvents] = useState([]);

  const [lang, ] = useState(
    localStorage.getItem('lang') || 'en'
  );

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

    function createCustomEventWithRouteParents(parentsArray) {
      const customEvents = parentsArray
        .map((event, index) => {
          return {
            image: event.image,
            title: `${langs['routes'][lang].single} #${index + 1}`,
            city: event.country,
            uuid: event.uuid
          }
        });
  
      return customEvents;
    }

    createRoutes();
  }, [lang]);


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

  return (
    <ListEvents title={langs['home'][lang].routes} typeIcon={routesIcon} eventsArray={events} isRoute={true}/>
  );
}

export default Routes;
