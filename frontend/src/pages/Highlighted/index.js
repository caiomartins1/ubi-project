import React from 'react';
import ListEvents from '../../components/ListEvents';

import highlightedIcon from '../../assets/icons/highlighted-icon.png';

import './index.css';

function Highlighted() {
  return (
    <ListEvents title="Highlighted" typeIcon={highlightedIcon}/>
  );
}

export default Highlighted;
