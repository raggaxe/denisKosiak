const options = {
    connection: {
      secure: true,
      reconnect: true
    },
    identity: {
      username: 'deniskosiak',
      password: 'YOUR_TWITCH_OAUTH_TOKEN'
    },
    channels: ['YOUR_TWITCH_CHANNEL']
  };
  
  const client = new tmi.Client(options);

  client.on('connected', (address, port) => {
    console.log(`Connected to Twitch Chat: ${address}:${port}`);
  });

  client.on('message', (channel, tags, message, self) => {
    if (self) return; // Ignore messages from the bot itself

    const chatMessages = document.getElementById('chatMessages');
    const listItem = document.createElement('li');
    listItem.textContent = `[${channel}] ${tags.username}: ${message}`;
    chatMessages.appendChild(listItem);
  });

  client.connect();
