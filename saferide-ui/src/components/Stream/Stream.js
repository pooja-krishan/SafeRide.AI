import React from 'react'
import "./Stream.css";

const Stream = () => {
  return (
    <div className="content">
        <div className='header'>
            <h1>Dashcam Video</h1>
            <h4>There is a <span>67%</span> chance of a conflict</h4>
        </div>
        <div className='video'>
            <video id="vidstream"><source src="vid_sample.mp4" type="video/mp4" /></video>
        </div>
        <div className="transcript">
            <h1>Transcript for the video</h1>
            <p className='textBody'>
                You are a moron
            </p>
            <p className='textBody'>
                I am not a moron
            </p>
        </div>
    </div>
  )
}

export default Stream