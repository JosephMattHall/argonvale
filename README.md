<div class="markdown prose w-full break-words dark:prose-invert light"><h1>Argonvale Adventures Backend</h1><p>Welcome to Argonvale Adventures, an exciting multiplayer online game where users can create companions, embark on adventures, chat with other players, train their companions, and engage in epic turn-based battles. Dive into a world of medieval fantasy, magic, and adventure as you build your team of companions and explore the realm of Argonvale.</p><h2>Table of Contents</h2><ol><li><a href="#introduction" target="_new">Introduction</a></li><li><a href="#project-description" target="_new">Project Description</a></li><li><a href="#features" target="_new">Features</a></li><li><a href="#technologies-used" target="_new">Technologies Used</a></li><li><a href="#getting-started" target="_new">Getting Started</a></li><li><a href="#api-endpoints" target="_new">API Endpoints</a></li><li><a href="#authentication" target="_new">Authentication</a></li><li><a href="#database" target="_new">Database</a></li><li><a href="#training-system" target="_new">Training System</a></li><li><a href="#contributing" target="_new">Contributing</a></li><li><a href="#license" target="_new">License</a></li></ol><h2>1. Introduction</h2><p>Argonvale Adventures is a virtual companion multiplayer online game designed for mobile devices and web browsers. This repository contains the backend server code that powers the game. It handles user registration and authentication, companion management, training, battles, and more.</p><h2>2. Project Description</h2><p>In the world of Argonvale, players can:</p><ul><li><p><strong>Create Companions:</strong> Users can create unique companions with distinct names, attributes, and abilities. Each companion is your loyal ally in battles and adventures.</p></li><li><p><strong>Embark on Adventures:</strong> Explore the enchanting realm of Argonvale, where you'll encounter mythical creatures, hidden treasures, and challenging quests. Use your companions' abilities to overcome obstacles and claim victory.</p></li><li><p><strong>Train Companions:</strong> Improve your companions' strength, defense, and speed by sending them to the training school. Higher-level companions require more training time, offering a strategic edge in battles.</p></li><li><p><strong>Engage in Battles:</strong> Challenge other players to real-time turn-based battles. Your companions' stats and abilities will determine your success in combat. Strategic planning and quick decision-making are key to victory.</p></li><li><p><strong>Collect Rare Items:</strong> Discover rare and valuable items during your adventures. Expand your collection and use them to enhance your companions' abilities.</p></li><li><p><strong>Trade in User Shops:</strong> Set up your own shop and trade items with other players. Build your wealth and acquire unique items to gain an advantage in battles.</p></li><li><p><strong>Join the Trading Post:</strong> Participate in a bustling marketplace where players buy, sell, and trade items. Hunt for bargains or negotiate deals with fellow adventurers.</p></li></ul><h2>3. Features</h2><ul><li>User Registration and Authentication</li><li>Companion Creation and Management</li><li>Adventure Exploration</li><li>Training School for Companions</li><li>Real-Time Turn-Based Battles</li><li>Item Collection and Trading</li><li>User Shops and Trading Post</li><li>Medieval Fantasy Theme</li></ul><h2>4. Technologies Used</h2><ul><li><a href="https://www.python.org/" target="_new">Python</a>: The backend server is written in Python 3.</li><li><a href="https://sanicframework.org/" target="_new">Sanic</a>: A fast asynchronous web framework for building APIs.</li><li><a href="https://www.mongodb.com/" target="_new">MongoDB</a>: A NoSQL database for storing user and game data.</li><li><a href="https://motor.readthedocs.io/" target="_new">Motor</a>: An asynchronous driver for MongoDB, used for database interactions.</li><li><a href="https://jwt.io/" target="_new">JSON Web Tokens (JWT)</a>: Used for user authentication and session management.</li></ul><h2>5. Getting Started</h2><p>To set up and run the Argonvale Adventures backend server on your local machine, follow these steps:</p><ol><li><p>Clone this repository to your local environment.</p></li><li><p>Create a <code>.env</code> file in the project directory and configure it with your MongoDB connection details and secret key.</p><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>makefile</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-makefile">MONGODB_HOST=#for development use localhost
MONGODB_PORT=# usually 27017
MONGODB_DBNAME=# i call mine game_database in development
SECRET_KEY=# this one is up to you
</code></div></div></pre></li><li><p>Install the required Python packages by running <code>pip install -r requirements.txt</code>.</p></li><li><p>Run the server using <code>python app.py</code>. The server will start on <code>http://localhost:8000</code>.</p></li></ol><h2>6. API Endpoints</h2><p>The server provides various API endpoints for user registration, authentication, companion management, training, battles, and more. Refer to the code comments and documentation for details on each endpoint.</p><h2>7. Authentication</h2><p>Argonvale Adventures uses JSON Web Tokens (JWT) for user authentication. Users can register and log in to obtain an access token, which they must include in the <code>Authorization</code> header when making authenticated requests.</p><h2>8. Database</h2><p>User and game data are stored in a MongoDB database using the Motor asynchronous driver. Companions, items, and user details are managed in the database to ensure a seamless gaming experience.</p><h2>9. Training System</h2><p>Companions can be sent to the training school to improve their attributes. The training duration varies based on the companion's level, providing a strategic element to the game.</p><h2>10. Contributing</h2><p>We welcome contributions from the community to help enhance Argonvale Adventures. Feel free to open issues, suggest improvements, or submit pull requests.</p><h2>11. License</h2><p>This project is licensed under the MIT License. See the <a href="LICENSE" target="_new">LICENSE</a> file for details.</p><p>Join the adventure in Argonvale, where mystical creatures, epic battles, and rare treasures await. Dive into the code, explore the realm, and embark on your journey today!</p></div>