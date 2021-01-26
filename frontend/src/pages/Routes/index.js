import React from 'react';
import ListEvents from '../../components/ListEvents';

import routesIcon from '../../assets/icons/routes-icon.png';

import './index.css';

function Routes() {
  return (
    <ListEvents title="Routes" typeIcon={routesIcon} />
  );
}

export default Routes;
