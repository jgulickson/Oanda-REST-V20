# !/usr/bin/env python

#
# Format Instrument Oanda
#
def format_instrument_oanda(instrument):
    instrument_length = len(instrument)
    if instrument_length == 7:
        if "_" in instrument:
            return str(instrument)
        elif "/" in instrument:
            return str(instrument.replace("/", "_"))
        elif "-" in instrument:
            return str(instrument.replace("-", "_"))
        elif " " in instrument:
            return str(instrument.replace(" ", "_"))
        else:
            raise ValueError("Instrument name validity could not be determined.")
    elif instrument_length == 6:
        return str(instrument[:3] + "_" + instrument[3:])
    else:
        raise ValueError("Instrument name is not valid.")


#
# Format Instrument Sentiment
#
def format_instrument_sentiment(instrument):
    instrument_length = len(instrument)
    if instrument_length == 6:
        return str(instrument)
    elif instrument_length == 7:
        if "_" in instrument:
            return str(instrument.replace("_", ""))
        elif "/" in instrument:
            return str(instrument.replace("/", ""))
        elif "-" in instrument:
            return str(instrument.replace("-", ""))
        elif " " in instrument:
            return str(instrument.replace(" ", ""))
        else:
            raise ValueError("Instrument name validity could not be determined.")
    else:
        raise ValueError("Instrument name is not valid.")


#
# Format Pips
#
def format_pips(pip_location):
    if pip_location == 0:
        return 1
    elif pip_location == -1:
        return .1
    elif pip_location == -2:
        return .01
    elif pip_location == -3:
        return .001
    elif pip_location == -4:
        return .0001
    elif pip_location == -5:
        return .00001
    else:
        raise ValueError("Pip location is invalid.")


#
# Format Precision
#
def format_precision(value, precision):
    return "{number:.{digits}f}".format(number = value, digits = precision)
