import React from 'react';
import ListEvents from '../../components/ListEvents';

import exploreIcon from '../../assets/icons/explore-icon.png';

import './index.css';

function App() {
  return (
    <ListEvents title="Explore" typeIcon={exploreIcon}/>
  );
}

export default App;
