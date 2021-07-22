function Top (rt) {
  this.libSet = new Set ()
  this.libs = []
  this.addLib = function (lib, decl) { if (!this.libSet.has (lib +'.'+decl)) { this.libSet.add (lib +'.'+decl); this.libs.push ({lib:lib, decl:decl})} }
  this.loadlibs = function (cb) { rt.linkLibs (this.libs, this, cb) }
  this.serializedatoms = "AQAAAAAAAAAA"
  this.gensym6 = function ($env,arg111) {
    const gensym8 = rt.mkCopy(rt.print);
    rt.tailcall (gensym8,$env.gensym11);
  }
  this.gensym6.deps = [];
  this.gensym6.libdeps = [];
  this.gensym6.serialized = "AAAAAAAAAAAHZ2Vuc3ltNgAAAAAAAAAGYXJnMTExAAAAAAAAAAEAAAAAAAAAAAdnZW5zeW04BgAAAAAAAAAFcHJpbnQAAAAAAAAAAAAHZ2Vuc3ltOAEAAAAAAAAACGdlbnN5bTEx";
  this.gensym3 = function ($env,arg16) {
    const gensym21 = rt.istuple(arg16);
    rt.push ((gensym16) =>
             {rt.branch (gensym16);
              if (rt.getVal(gensym16)) {
                const gensym12 = rt.mkValPos (0,'RTGen<CaseElimination>');;
                const gensym11 = rt.index (arg16,gensym12);;
                const gensym5 = rt.mkValPos (0,'RTGen<CaseElimination>');;
                const $$$env0 = new rt.Env();
                $$$env0.gensym11 = gensym11;
                const gensym6 = rt.mkVal(new rt.Closure($$$env0, this, this.gensym6))
                $$$env0.gensym6 = gensym6;
                $$$env0.gensym6.selfpointer = true;
                const gensym7 = rt.mkVal(rt.mkTuple([gensym5, gensym6]));
                rt.ret (gensym7);
              } else {
                const gensym13 = rt.mkValPos (1,'RTGen<CaseElimination>');;
                const gensym14 = rt.__unit;
                const gensym15 = rt.mkVal(rt.mkTuple([gensym13, gensym14]));
                rt.ret (gensym15);
              }});
    rt.branch (gensym21);
    if (rt.getVal(gensym21)) {
      const gensym18 = rt.length(arg16);
      const gensym19 = rt.mkValPos (2,'RTGen<CaseElimination>');;
      const gensym17 = rt.eq (gensym18,gensym19);;
      rt.ret (gensym17);
    } else {
      const gensym20 = rt.mkValPos (false,'');;
      rt.ret (gensym20);
    }
  }
  this.gensym3.deps = ['gensym6'];
  this.gensym3.libdeps = [];
  this.gensym3.serialized = "AAAAAAAAAAAHZ2Vuc3ltMwAAAAAAAAAFYXJnMTYAAAAAAAAAAQAAAAAAAAAACGdlbnN5bTIxAQEAAAAAAAAAAAVhcmcxNgYAAAAAAAAACGdlbnN5bTE2AAAAAAAAAAACAAAAAAAAAAAIZ2Vuc3ltMjEAAAAAAAAAAwAAAAAAAAAACGdlbnN5bTE4AQYAAAAAAAAAAAVhcmcxNgAAAAAAAAAACGdlbnN5bTE5BQAAAAAAAgEAAAAAAAAAD0Nhc2VFbGltaW5hdGlvbgAAAAAAAAAACGdlbnN5bTE3AAUAAAAAAAAAAAhnZW5zeW0xOAAAAAAAAAAACGdlbnN5bTE5AQAAAAAAAAAACGdlbnN5bTE3AAAAAAAAAAEAAAAAAAAAAAhnZW5zeW0yMAUEAAEAAAAAAAAAAAhnZW5zeW0yMAAAAAAAAAAAAgAAAAAAAAAACGdlbnN5bTE2AAAAAAAAAAUAAAAAAAAAAAhnZW5zeW0xMgUAAAAAAAABAAAAAAAAAA9DYXNlRWxpbWluYXRpb24AAAAAAAAAAAhnZW5zeW0xMQANAAAAAAAAAAAFYXJnMTYAAAAAAAAAAAhnZW5zeW0xMgAAAAAAAAAAB2dlbnN5bTUFAAAAAAAAAQAAAAAAAAAPQ2FzZUVsaW1pbmF0aW9uAQAAAAAAAAABAAAAAAAAAAhnZW5zeW0xMQAAAAAAAAAACGdlbnN5bTExAAAAAAAAAAEAAAAAAAAAB2dlbnN5bTYAAAAAAAAAB2dlbnN5bTYAAAAAAAAAAAdnZW5zeW03AgAAAAAAAAACAAAAAAAAAAAHZ2Vuc3ltNQAAAAAAAAAAB2dlbnN5bTYBAAAAAAAAAAAHZ2Vuc3ltNwAAAAAAAAADAAAAAAAAAAAIZ2Vuc3ltMTMFAAAAAAABAQAAAAAAAAAPQ2FzZUVsaW1pbmF0aW9uAAAAAAAAAAAIZ2Vuc3ltMTQFAwAAAAAAAAAACGdlbnN5bTE1AgAAAAAAAAACAAAAAAAAAAAIZ2Vuc3ltMTMAAAAAAAAAAAhnZW5zeW0xNAEAAAAAAAAAAAhnZW5zeW0xNQ==";
  this.main = function ($env,$$authorityarg) {
    rt.push (($decltemp$2) =>
             {rt.push (($decltemp$4) =>
                       {const gensym2 = rt.mkCopy(rt.receive);
                        const $$$env1 = new rt.Env();
                        const gensym3 = rt.mkVal(new rt.Closure($$$env1, this, this.gensym3))
                        $$$env1.gensym3 = gensym3;
                        $$$env1.gensym3.selfpointer = true;
                        const gensym4 = rt.mkVal(rt.mkList([gensym3]));
                        rt.push ((gensym1) =>
                                 {rt.ret (gensym1);});
                        rt.tailcall (gensym2,gensym4);});
              const gensym22 = rt.mkCopy(rt.send);
              const gensym23 = rt.mkValPos ("ECHO",'');;
              const gensym24 = rt.mkValPos ("Hello",'');;
              const gensym28 = rt.mkCopy(rt.self);
              const gensym29 = rt.__unit;
              rt.push ((gensym25) =>
                       {const gensym26 = rt.mkVal(rt.mkTuple([gensym23, gensym24, gensym25]));
                        const gensym27 = rt.mkVal(rt.mkTuple([$decltemp$2, gensym26]));
                        rt.tailcall (gensym22,gensym27);});
              rt.tailcall (gensym28,gensym29);});
    const gensym30 = rt.mkCopy(rt.whereis);
    const gensym31 = rt.mkValPos ("QmTi7KZUeWG8rgamV2tdU7FdED7GZ8MubPQc6fcpNeyQVJ",'');;
    const gensym32 = rt.mkValPos ("echo",'');;
    const gensym33 = rt.mkVal(rt.mkTuple([gensym31, gensym32]));
    rt.tailcall (gensym30,gensym33);
  }
  this.main.deps = ['gensym3'];
  this.main.libdeps = [];
  this.main.serialized = "AAAAAAAAAAAEbWFpbgAAAAAAAAAOJCRhdXRob3JpdHlhcmcAAAAAAAAAAAYAAAAAAAAACyRkZWNsdGVtcCQyAAAAAAAAAAQAAAAAAAAAAAhnZW5zeW0zMAYAAAAAAAAAB3doZXJlaXMAAAAAAAAAAAhnZW5zeW0zMQUBAAAAAAAAAC5RbVRpN0taVWVXRzhyZ2FtVjJ0ZFU3RmRFRDdHWjhNdWJQUWM2ZmNwTmV5UVZKAAAAAAAAAAAIZ2Vuc3ltMzIFAQAAAAAAAAAEZWNobwAAAAAAAAAACGdlbnN5bTMzAgAAAAAAAAACAAAAAAAAAAAIZ2Vuc3ltMzEAAAAAAAAAAAhnZW5zeW0zMgAAAAAAAAAAAAhnZW5zeW0zMAAAAAAAAAAACGdlbnN5bTMzAAAAAAAAAAAGAAAAAAAAAAskZGVjbHRlbXAkNAAAAAAAAAAFAAAAAAAAAAAIZ2Vuc3ltMjIGAAAAAAAAAARzZW5kAAAAAAAAAAAIZ2Vuc3ltMjMFAQAAAAAAAAAERUNITwAAAAAAAAAACGdlbnN5bTI0BQEAAAAAAAAABUhlbGxvAAAAAAAAAAAIZ2Vuc3ltMjgGAAAAAAAAAARzZWxmAAAAAAAAAAAIZ2Vuc3ltMjkFAwYAAAAAAAAACGdlbnN5bTI1AAAAAAAAAAAAAAAAAAAAAAAIZ2Vuc3ltMjgAAAAAAAAAAAhnZW5zeW0yOQAAAAAAAAACAAAAAAAAAAAIZ2Vuc3ltMjYCAAAAAAAAAAMAAAAAAAAAAAhnZW5zeW0yMwAAAAAAAAAACGdlbnN5bTI0AAAAAAAAAAAIZ2Vuc3ltMjUAAAAAAAAAAAhnZW5zeW0yNwIAAAAAAAAAAgAAAAAAAAAACyRkZWNsdGVtcCQyAAAAAAAAAAAIZ2Vuc3ltMjYAAAAAAAAAAAAIZ2Vuc3ltMjIAAAAAAAAAAAhnZW5zeW0yNwAAAAAAAAADAAAAAAAAAAAHZ2Vuc3ltMgYAAAAAAAAAB3JlY2VpdmUBAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAHZ2Vuc3ltMwAAAAAAAAAHZ2Vuc3ltMwAAAAAAAAAAB2dlbnN5bTQDAAAAAAAAAAEAAAAAAAAAAAdnZW5zeW0zBgAAAAAAAAAHZ2Vuc3ltMQAAAAAAAAAAAAAAAAAAAAAAB2dlbnN5bTIAAAAAAAAAAAdnZW5zeW00AAAAAAAAAAABAAAAAAAAAAAHZ2Vuc3ltMQ==";
}
module.exports = Top 