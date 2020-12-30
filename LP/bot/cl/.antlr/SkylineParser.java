// Generated from c:\Users\Fede\Desktop\FIB UPC\LP\TelegramBot\cl\Skyline.g by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, NUM=9, 
		ID=10, MULT=11, SUB=12, ADD=13, WS=14;
	public static final int
		RULE_root = 0, RULE_assign = 1, RULE_constructor = 2, RULE_edifici = 3, 
		RULE_op = 4;
	public static final String[] ruleNames = {
		"root", "assign", "constructor", "edifici", "op"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "':='", "'['", "','", "']'", "'{'", "'}'", "'('", "')'", null, null, 
		"'*'", "'-'", "'+'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, "NUM", "ID", "MULT", 
		"SUB", "ADD", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Skyline.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SkylineParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SkylineParser.EOF, 0); }
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			setState(16);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(10);
				assign();
				setState(11);
				match(EOF);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(13);
				op(0);
				setState(14);
				match(EOF);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SkylineParser.ID, 0); }
		public ConstructorContext constructor() {
			return getRuleContext(ConstructorContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_assign);
		try {
			setState(24);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				match(ID);
				setState(19);
				match(T__0);
				setState(20);
				constructor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(21);
				match(ID);
				setState(22);
				match(T__0);
				setState(23);
				op(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstructorContext extends ParserRuleContext {
		public List<EdificiContext> edifici() {
			return getRuleContexts(EdificiContext.class);
		}
		public EdificiContext edifici(int i) {
			return getRuleContext(EdificiContext.class,i);
		}
		public List<TerminalNode> NUM() { return getTokens(SkylineParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(SkylineParser.NUM, i);
		}
		public ConstructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructor; }
	}

	public final ConstructorContext constructor() throws RecognitionException {
		ConstructorContext _localctx = new ConstructorContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_constructor);
		int _la;
		try {
			setState(49);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				edifici();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				match(T__1);
				setState(28);
				edifici();
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__2) {
					{
					{
					setState(29);
					match(T__2);
					setState(30);
					edifici();
					}
					}
					setState(35);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(36);
				match(T__3);
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				match(T__4);
				setState(39);
				match(NUM);
				setState(40);
				match(T__2);
				setState(41);
				match(NUM);
				setState(42);
				match(T__2);
				setState(43);
				match(NUM);
				setState(44);
				match(T__2);
				setState(45);
				match(NUM);
				setState(46);
				match(T__2);
				setState(47);
				match(NUM);
				setState(48);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EdificiContext extends ParserRuleContext {
		public List<TerminalNode> NUM() { return getTokens(SkylineParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(SkylineParser.NUM, i);
		}
		public EdificiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edifici; }
	}

	public final EdificiContext edifici() throws RecognitionException {
		EdificiContext _localctx = new EdificiContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_edifici);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(T__6);
			setState(52);
			match(NUM);
			setState(53);
			match(T__2);
			setState(54);
			match(NUM);
			setState(55);
			match(T__2);
			setState(56);
			match(NUM);
			setState(57);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OpContext extends ParserRuleContext {
		public List<OpContext> op() {
			return getRuleContexts(OpContext.class);
		}
		public OpContext op(int i) {
			return getRuleContext(OpContext.class,i);
		}
		public TerminalNode SUB() { return getToken(SkylineParser.SUB, 0); }
		public TerminalNode ID() { return getToken(SkylineParser.ID, 0); }
		public ConstructorContext constructor() {
			return getRuleContext(ConstructorContext.class,0);
		}
		public TerminalNode MULT() { return getToken(SkylineParser.MULT, 0); }
		public TerminalNode ADD() { return getToken(SkylineParser.ADD, 0); }
		public TerminalNode NUM() { return getToken(SkylineParser.NUM, 0); }
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
	}

	public final OpContext op() throws RecognitionException {
		return op(0);
	}

	private OpContext op(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		OpContext _localctx = new OpContext(_ctx, _parentState);
		OpContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_op, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(60);
				match(T__6);
				setState(61);
				op(0);
				setState(62);
				match(T__7);
				}
				break;
			case 2:
				{
				setState(64);
				match(SUB);
				setState(65);
				op(8);
				}
				break;
			case 3:
				{
				setState(66);
				match(ID);
				}
				break;
			case 4:
				{
				setState(67);
				constructor();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(87);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(85);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new OpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_op);
						setState(70);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(71);
						match(MULT);
						setState(72);
						op(8);
						}
						break;
					case 2:
						{
						_localctx = new OpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_op);
						setState(73);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(74);
						match(ADD);
						setState(75);
						op(4);
						}
						break;
					case 3:
						{
						_localctx = new OpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_op);
						setState(76);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(77);
						match(MULT);
						setState(78);
						match(NUM);
						}
						break;
					case 4:
						{
						_localctx = new OpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_op);
						setState(79);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(80);
						match(ADD);
						setState(81);
						match(NUM);
						}
						break;
					case 5:
						{
						_localctx = new OpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_op);
						setState(82);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(83);
						match(SUB);
						setState(84);
						match(NUM);
						}
						break;
					}
					} 
				}
				setState(89);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return op_sempred((OpContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean op_sempred(OpContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		case 4:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20]\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\2\3\2\3\2\5\2\23\n\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\5\3\33\n\3\3\4\3\4\3\4\3\4\3\4\7\4\"\n\4\f\4\16\4%\13"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64\n\4\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6G"+
		"\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6X"+
		"\n\6\f\6\16\6[\13\6\3\6\2\3\n\7\2\4\6\b\n\2\2\2d\2\22\3\2\2\2\4\32\3\2"+
		"\2\2\6\63\3\2\2\2\b\65\3\2\2\2\nF\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16"+
		"\23\3\2\2\2\17\20\5\n\6\2\20\21\7\2\2\3\21\23\3\2\2\2\22\f\3\2\2\2\22"+
		"\17\3\2\2\2\23\3\3\2\2\2\24\25\7\f\2\2\25\26\7\3\2\2\26\33\5\6\4\2\27"+
		"\30\7\f\2\2\30\31\7\3\2\2\31\33\5\n\6\2\32\24\3\2\2\2\32\27\3\2\2\2\33"+
		"\5\3\2\2\2\34\64\5\b\5\2\35\36\7\4\2\2\36#\5\b\5\2\37 \7\5\2\2 \"\5\b"+
		"\5\2!\37\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%#\3\2\2\2&\'"+
		"\7\6\2\2\'\64\3\2\2\2()\7\7\2\2)*\7\13\2\2*+\7\5\2\2+,\7\13\2\2,-\7\5"+
		"\2\2-.\7\13\2\2./\7\5\2\2/\60\7\13\2\2\60\61\7\5\2\2\61\62\7\13\2\2\62"+
		"\64\7\b\2\2\63\34\3\2\2\2\63\35\3\2\2\2\63(\3\2\2\2\64\7\3\2\2\2\65\66"+
		"\7\t\2\2\66\67\7\13\2\2\678\7\5\2\289\7\13\2\29:\7\5\2\2:;\7\13\2\2;<"+
		"\7\n\2\2<\t\3\2\2\2=>\b\6\1\2>?\7\t\2\2?@\5\n\6\2@A\7\n\2\2AG\3\2\2\2"+
		"BC\7\16\2\2CG\5\n\6\nDG\7\f\2\2EG\5\6\4\2F=\3\2\2\2FB\3\2\2\2FD\3\2\2"+
		"\2FE\3\2\2\2GY\3\2\2\2HI\f\t\2\2IJ\7\r\2\2JX\5\n\6\nKL\f\5\2\2LM\7\17"+
		"\2\2MX\5\n\6\6NO\f\b\2\2OP\7\r\2\2PX\7\13\2\2QR\f\7\2\2RS\7\17\2\2SX\7"+
		"\13\2\2TU\f\6\2\2UV\7\16\2\2VX\7\13\2\2WH\3\2\2\2WK\3\2\2\2WN\3\2\2\2"+
		"WQ\3\2\2\2WT\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\13\3\2\2\2[Y\3\2\2"+
		"\2\t\22\32#\63FWY";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}