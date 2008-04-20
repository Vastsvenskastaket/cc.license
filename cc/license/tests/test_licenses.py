from nose.tools import assert_true

def test_find_sampling_selector():
    from zope.interface import implementedBy
    import cc.license

    sampling_selector = cc.license.get_selector('recombo')()
    return sampling_selector

def test_find_sampling_licenses():
    selector = test_find_sampling_selector()
    lic = selector.by_code('sampling')
    assert_true(not lic.libre)
    assert_true(lic.deprecated)
    lic = selector.by_code('sampling+')
    assert_true(not lic.deprecated)

def test_find_pd():
    from zope.interface import implementedBy
    import cc.license

    pd_selector = cc.license.get_selector('publicdomain')()
    pd = pd_selector.by_code('publicdomain')
    return pd

def test_pd():
    pd = test_find_pd()
    assert_true(pd.libre)
    assert_true(pd.jurisdiction == 'Your mom')
    assert_true(not pd.deprecated)
    assert_true(pd.jurisdiction == 'Your mom')
    assert_true(pd.license_code == 'publicdomain')
    assert_true(pd.name() == 'Public Domain' == pd.name('en'))
    assert_true(pd.name('hr') == u'Javna domena')
