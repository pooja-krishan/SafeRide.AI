import React from 'react'
import "./Stream.css";

const Stream = ({transcript,prediction}) => {
  return (
    <div className="content">
        <div className='header'>
            <h1>Dashcam Video</h1>
            <h4>There is a <span>{prediction}</span> chance of a conflict</h4>
        </div>
        <div className='video'>
            {/* <video id="vidstream"><source src="vid_sample.mp4" type="video/mp4" /></video> */}
            <img src={"http://127.0.0.1:5000/stream"} />
        </div>
        <div className="transcript">
            <h1>Transcript for the video</h1>
            {transcript.map((item) => {
                return(
                    <p className="textBody">{item}</p>
                )
            })}
        </div>
    </div>
  )
}

export default Stream