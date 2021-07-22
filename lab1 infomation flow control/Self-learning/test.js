function Top (rt) {
  this.libSet = new Set ()
  this.libs = []
  this.addLib = function (lib, decl) { if (!this.libSet.has (lib +'.'+decl)) { this.libSet.add (lib +'.'+decl); this.libs.push ({lib:lib, decl:decl})} }
  this.loadlibs = function (cb) { rt.linkLibs (this.libs, this, cb) }
  this.serializedatoms = "AQAAAAAAAAAA"
  this.main = function ($env,$$authorityarg) {
    const gensym3 = rt.mkLabel("bob");
    const gensym2 = rt.mkValPos (1,':164:17');;
    const gensym1 = rt.raisedTo (gensym2,gensym3);;
    rt.ret (gensym1);
  }
  this.main.deps = [];
  this.main.libdeps = [];
  this.main.serialized = "AAAAAAAAAAAEbWFpbgAAAAAAAAAOJCRhdXRob3JpdHlhcmcAAAAAAAAAAwAAAAAAAAAAB2dlbnN5bTMFAgAAAAAAAAADYm9iAAAAAAAAAAAHZ2Vuc3ltMgUAAAAAAAEAAAAAAAAAAAAAAAAAAAAApAAAAAAAAAARAAAAAAAAAAAHZ2Vuc3ltMQAOAAAAAAAAAAAHZ2Vuc3ltMgAAAAAAAAAAB2dlbnN5bTMBAAAAAAAAAAAHZ2Vuc3ltMQ==";
}
module.exports = Top 