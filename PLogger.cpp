#include <iostream>
#include <string>


using std::cout;
using std::cerr;
using std::endl;


class PLogger
{
public:
	enum class LOG_LEVEL { NONE=-1, DEBUG, INFO, WARNING, ERROR };
	PLogger() : level(LOG_LEVEL::NONE) {}
	PLogger(LOG_LEVEL level) : level(level) {}
	virtual ~PLogger() {}

	virtual int get_level() const { return static_cast<int>(level); }
	virtual void set_level(LOG_LEVEL lvl) { level = lvl; }

	virtual void debug(const std::string& msg) { base_log(msg, LOG_LEVEL::DEBUG); }
	virtual void info(const std::string& msg) { base_log(msg, LOG_LEVEL::INFO); }
	virtual void warn(const std::string& msg) { base_log(msg, LOG_LEVEL::WARNING); }
	virtual void warning(const std::string& msg) { base_log(msg, LOG_LEVEL::WARNING); }
	virtual void error(const std::string& msg) { base_log(msg, LOG_LEVEL::ERROR); }
	virtual void exception(const std::string& msg, const std::string& what) { base_log(msg+" Stacktrace: "+what, LOG_LEVEL::ERROR); }

protected:
	void base_log(const std::string& msg, LOG_LEVEL function_level)
	{
		switch (function_level)
		{
		case PLogger::LOG_LEVEL::DEBUG:
			if (level <= LOG_LEVEL::DEBUG)
				cout << msg << endl;
			break;
		case PLogger::LOG_LEVEL::INFO:
			if (level <= LOG_LEVEL::INFO)
				cout << msg << endl;
			break;
		case PLogger::LOG_LEVEL::WARNING:
			if (level <= LOG_LEVEL::WARNING)
				cout << msg << endl;
			break;
		case PLogger::LOG_LEVEL::ERROR:
			if (level <= LOG_LEVEL::ERROR)
				cerr << msg << endl;
			break;
		default:
			cout << "PLogger::base_log - NO LOG LEVEL SET.\n" << endl;
			break;
		}
	}

	LOG_LEVEL level;
};


int main()
{
	PLogger logger(PLogger::LOG_LEVEL::INFO);

	logger.debug("DEBUG");
	logger.info("INFO");
	logger.warn("WARN");
	logger.error("ERROR");

	try
	{
		throw std::exception("MY EXCEPTION");
	}
	catch (std::exception& ex)
	{
		logger.exception("Exception Occurred.", ex.what());
	}

	cout << "Hello World" << endl;

	return 0;
}
