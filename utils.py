"""
    func windDirectionFromDegrees(degrees : Float) -> String {

    let directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    let i: Int = Int((degrees + 11.25)/22.5)
    return directions[i % 16]
}
"""

LAT = "43.2348"
LONG = "-2.8827"


def degrees_to_direction(grados):
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"]
    index = int((grados + 11.25) / 22.5)
    return dirs[index]


def get_air_quality(value):
    if value == 1:
        return "MUY BUENA"
    elif value == 2:
        return "BUENA"
    elif value == 3:
        return "NORMAL"
    elif value == 4:
        return "MEDIOCRE"
    elif value == 5:
        return "MALA"
    else:
        return "NO DATA"
