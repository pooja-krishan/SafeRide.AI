import logo from './logo.svg';
import './App.css';
import { useState,useEffect } from "react";
import { Navbar } from './components/Navbar/Navbar';
import Stream from './components/Stream/Stream';
import axios from "axios";
const App = () => {
  const [transcript, setTranscript] = useState([]);
  const [prediction, setPrediction] = useState(0);

  const updateTranscript = async() => {
    axios({method: "GET", url:"http://127.0.0.1:5000/transcript"}).then((response => {
      console.log(response)
    })).catch((error) => {
      console.log(error.message)
    })
    // setTrtranscript.concat(response.data));
  }
  useEffect(() => {
    updateTranscript();
  },[])

  return (
    <div>
      <Navbar />
      <Stream transcript={transcript} prediction={prediction} />
    </div>

  )
}

export default App;
