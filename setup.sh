mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"roro.silva99999@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#FF0000'\n\
backgroundColor = '#00325B'\n\
secondaryBackgroundColor = '#55B2FF'\n\
textColor = "#FFFFFF"\n\
" > ~/.streamlit/config.toml