import React, {useState} from 'react'
import Axios from 'axios';
function App() {
    const [inputText, setInputText] = useState("");
    const [data, setData] = useState([]);
    const handle = (e) =>{
        e.preventDefault();
        console.log(inputText);
        setInputText(e.target.value)
        console.log(inputText);
    }
    const getData = (e) =>{
        e.preventDefault()
        Axios.get('/getResult').then(res =>{
            console.log("Getting from ::::", res.data)
            setData(res.data)
        }).catch(err => console.log(err))
    }
    const postData = (e) =>{
        e.preventDefault();
        Axios.post('postLink', {
            inputText
        }).then(res =>
            console.log("Posting data ::::", res)
        ).catch(err => console.log(err))
    }


  return (
    <div className="App">
        <h1>Youtube Downloader</h1>
        <input
                  placeholder="Please enter the video URL"
                  type="text"
                  value={inputText}
                  id="outlined-basic"
                  onChange={handle}
                  variant="outlined"
                  fullWidth
                  label="Search"
                  name="inputText"
                  onChangeCapture={postLink}
        /><button className="btnPost"  onClickCapture={getResult}>
                  <i className="fas fa-search">Download</i>
              </button>
        <div className="groupButton">
            {/*<button className="btnGet" onClick={getData}>
                  <i className="fas fa-search">Result</i>
              </button>*/}
        </div>
        <div className="result">
           <ul>
                {( typeof data.paths === 'undefined') ? (
                    <p>Loading...</p>
                ) : (
                    data.paths.map((item, i) => (
                        <li key={i}>{item}</li>
                    ))
                )}
            </ul>
            </div>
    </div>
  );
}

export default App;
