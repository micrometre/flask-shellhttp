import { createEffect, createSignal, createResource, Switch, Match, Show } from "solid-js";

import styles from './App.module.css';

const buttons = [{
  command: "uptime",
  name: "uptime",
  id: 1
},
{
  command: "uname",
  name: "uname",
  id: 2
},
{
  command: "pwd",
  name: "pwd",
  id: 2
}

];

async function exeCmd() {

};

function App() {
  async function handler(data, event) {
    try {
      const response = await fetch('http://127.0.0.1:5000/cmd/test', {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json',
           'Authorization': `Basic ${btoa('ubuntu:ubuntu')}` 

          
          },  
        body: JSON.stringify({ message: [handler, data]})
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();

    } catch (error) {
      console.error('Error:', error);
    }
    console.log(data);
  }

  return (
    <div class={styles.App}>
      <div class={styles.header}  >
        {buttons.map(command => (
          <div class={styles.header} key={command.id}>
            <button
              class={styles.cmdbtn}
              type="button" onClick={[handler, command.name]}
            >
              {command.name}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;

