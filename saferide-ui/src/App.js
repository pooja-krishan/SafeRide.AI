import logo from './logo.svg';
import './App.css';
import { Navbar } from './components/Navbar/Navbar';
import Stream from './components/Stream/Stream';

const App = () => {
  return (
    <div>
      <Navbar />
      <Stream />
    </div>

  )
}

export default App;
