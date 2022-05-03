import io

import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout


class MyApp:
    def __init__(self, medicalList, widget, userCoordinate):
        self.widget = widget
        self.widget.setWindowTitle('Shops are here')
        self.window_width, self.window_height = 900, 850
        self.widget.setMinimumSize(self.window_width, self.window_height)
        self.widget.setStyleSheet("background-color: #fff;")
        layout = QVBoxLayout()
        self.widget.setLayout(layout)

        m = folium.Map(
            zoom_start=13,
            location=userCoordinate,
            width=900, height=850
        )
        folium.Marker(
            location=userCoordinate,
            icon=folium.DivIcon(html=f""" <div><svg width="35" height="35" viewBox="0 0 32 32" fill="none" 
                        xmlns="http://www.w3.org/2000/svg"> <path d="M16 2C13.0837 2.00344 10.2878 3.16347 8.22564 
                        5.22563C6.16348 7.28778 5.00345 10.0837 5.00001 13C4.99652 15.3832 5.77499 17.7018 7.21601 19.6C7.21601 
                        19.6 7.51601 19.995 7.56501 20.052L16 30L24.439 20.047C24.483 19.994 24.784 19.6 24.784 19.6L24.785 
                        19.597C26.2253 17.6996 27.0034 15.3821 27 13C26.9966 10.0837 25.8365 7.28778 23.7744 5.22563C21.7122 
                        3.16347 18.9163 2.00344 16 2V2ZM16 17C15.2089 17 14.4355 16.7654 13.7777 16.3259C13.1199 15.8864 12.6072 
                        15.2616 12.3045 14.5307C12.0017 13.7998 11.9225 12.9956 12.0769 12.2196C12.2312 11.4437 12.6122 10.731 
                        13.1716 10.1716C13.731 9.61216 14.4437 9.2312 15.2197 9.07686C15.9956 8.92252 16.7998 9.00173 17.5307 
                        9.30448C18.2616 9.60723 18.8864 10.1199 19.3259 10.7777C19.7654 11.4355 20 12.2089 20 13C19.9987 14.0605 
                        19.5768 15.0771 18.827 15.827C18.0771 16.5768 17.0605 16.9987 16 17V17Z" fill="#000"/> </svg> 
                        </div>""")
        ).add_to(m)
        for i in medicalList:
            html = f"""
                   <h1> {i.get('name')}</h1>
                   <h2>{i.get("medical_name")}</h2>
                   <div>
                    <p>price: {i.get('price')}</p> 
                    <p>Quantity: {i.get('quantity')}</p>
                   </div>
                   """
            iframe = folium.IFrame(html=html, width=200, height=200)
            popup = folium.Popup(iframe, max_width=560)
            folium.Marker(
                location=[i.get("latitude"), i.get("longitude")],
                popup=popup,
                icon=folium.DivIcon(html=f""" <div><svg width="35" height="35" viewBox="0 0 32 32" fill="none" 
                xmlns="http://www.w3.org/2000/svg"> <path d="M16 2C13.0837 2.00344 10.2878 3.16347 8.22564 
                5.22563C6.16348 7.28778 5.00345 10.0837 5.00001 13C4.99652 15.3832 5.77499 17.7018 7.21601 19.6C7.21601 
                19.6 7.51601 19.995 7.56501 20.052L16 30L24.439 20.047C24.483 19.994 24.784 19.6 24.784 19.6L24.785 
                19.597C26.2253 17.6996 27.0034 15.3821 27 13C26.9966 10.0837 25.8365 7.28778 23.7744 5.22563C21.7122 
                3.16347 18.9163 2.00344 16 2V2ZM16 17C15.2089 17 14.4355 16.7654 13.7777 16.3259C13.1199 15.8864 12.6072 
                15.2616 12.3045 14.5307C12.0017 13.7998 11.9225 12.9956 12.0769 12.2196C12.2312 11.4437 12.6122 10.731 
                13.1716 10.1716C13.731 9.61216 14.4437 9.2312 15.2197 9.07686C15.9956 8.92252 16.7998 9.00173 17.5307 
                9.30448C18.2616 9.60723 18.8864 10.1199 19.3259 10.7777C19.7654 11.4355 20 12.2089 20 13C19.9987 14.0605 
                19.5768 15.0771 18.827 15.827C18.0771 16.5768 17.0605 16.9987 16 17V17Z" fill="#009c6d"/> </svg> 
                </div>""")
            ).add_to(m)
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        webView.resize(900, 850)
        layout.addWidget(webView)
